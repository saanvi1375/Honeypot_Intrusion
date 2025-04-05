import React, { useEffect, useState } from "react";
import axios from "axios";

const LogTable = () => {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5050/logs")
      .then(res => setLogs(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Honeypot Logs</h1>
      <table className="min-w-full border">
      <thead>
  <tr className="bg-gray-200">
    <th className="p-2 border">IP</th>
    <th className="p-2 border">Port</th>
    <th className="p-2 border">Timestamp</th>
    <th className="p-2 border">Description</th>
    <th className="p-2 border">Severity</th>
    <th className="p-2 border">Location</th>
    <th className="p-2 border">WHOIS</th>
  </tr>
</thead>
<tbody>
  {logs.map((log, index) => (
    <tr key={index} className="text-sm border-b">
      <td className="p-2 border">{log.ip}</td>
      <td className="p-2 border">{log.port}</td>
      <td className="p-2 border">{new Date(log.timestamp).toLocaleString()}</td>
      <td className="p-2 border">{log.description}</td>
      <td className="p-2 border">{log.severity}</td>
      <td className="p-2 border">
        {log.geo?.city || ''}, {log.geo?.region || ''}, {log.geo?.country || ''}
      </td>
      <td className="p-2 border">
        {log.whois?.asn_description || ''}<br />
        {log.whois?.network_name || ''}<br />
        {log.whois?.org || ''}
      </td>
    </tr>
  ))}
</tbody>

      </table>
    </div>
  );
};

export default LogTable;