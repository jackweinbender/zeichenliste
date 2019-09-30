import React from "react"

export default ({ title, stats, total }) => {
  const val = ({ node }) => {
    const pct = Math.floor((node.freq / total) * 100)
    return (
      <tr>
        <td>{node.value}</td>
        <td>{node.freq}</td>
        <td>
          <span class="chart-bar" style={{ width: `${pct * 0.8}%` }}>
            &nbsp;
          </span>
          <span class="chart-bar-pct">{pct}</span>
          {/* <progress max={total} value={value.freq}></progress> */}
        </td>
      </tr>
    )
  }
  return (
    <div className="stats-section">
      <h3 className="title">{title}</h3>
      <table>
        <thead>
          <tr>
            <th>Sign Value</th>
            <th>Freq.</th>
            <th></th>
          </tr>
        </thead>
        <tbody>{stats.sort((a, b) => b.node.freq - a.node.freq).map(v => val(v))}</tbody>
        <tfoot>
          <tr>
            <td>Total</td>
            <td>{total}</td>
            <td></td>
          </tr>
        </tfoot>
      </table>
    </div>
  )
}
