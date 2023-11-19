// search_frontend/src/App.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css'; // Import your CSS file for styling

const App = () => {
  const [logs, setLogs] = useState([]);
  const [query, setQuery] = useState('');
  const [dateRange, setDateRange] = useState({ start: '', end: '' });
  const [regexSearch, setRegexSearch] = useState(false);
  const [filters, setFilters] = useState({
    level: '',
    message: '',
    resourceId: '',
    timestamp: '',
    traceId: '',
    spanId: '',
    commit: '',
    parentResourceId: '',
  });

  const fetchLogs = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/search`, {
        params: { q: query, dateRange, regexSearch, ...filters },
      });
      setLogs(response.data);
    } catch (error) {
      console.error('Error fetching logs:', error);
    }
  };

  useEffect(() => {
    fetchLogs();
  }, [query, dateRange, regexSearch, filters]);

  return (
    <div className="app-container">
      <header>
        <h1>Log Viewer</h1>
      </header>
      <section className="search-section">
        <div>
          <label>
            Search:
            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
            />
          </label>
        </div>
        <div>
          <label>
            Date Range:
            <input
              type="date"
              value={dateRange.start}
              onChange={(e) => setDateRange({ ...dateRange, start: e.target.value })}
            />
            -
            <input
              type="date"
              value={dateRange.end}
              onChange={(e) => setDateRange({ ...dateRange, end: e.target.value })}
            />
          </label>
        </div>
        <div>
          <label>
            Regular Expression Search:
            <input
              type="checkbox"
              checked={regexSearch}
              onChange={(e) => setRegexSearch(e.target.checked)}
            />
          </label>
        </div>
        <div className="filter-section">
          <h2>Filters:</h2>
          <label>
            Level:
            <input
              type="text"
              value={filters.level}
              onChange={(e) => setFilters({ ...filters, level: e.target.value })}
            />
          </label>
          <label>
            Message:
            <input
              type="text"
              value={filters.message}
              onChange={(e) => setFilters({ ...filters, message: e.target.value })}
            />
          </label>
          <label>
            Resource ID:
            <input
              type="text"
              value={filters.resourceId}
              onChange={(e) => setFilters({ ...filters, resourceId: e.target.value })}
            />
          </label>
          {/* Add similar input fields for other filters */}
        </div>
      </section>
      <section className="log-section">
        <ul>
          {logs.map(log => (
            <li key={log.id}>
              {log.level} - {log.message} - {log.resourceId}
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
};

export default App;
