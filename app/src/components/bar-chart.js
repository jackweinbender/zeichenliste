import React from "react"

export default ({ title, stats, total }) => {
  const val = value => (
    <tr>
      <td>{value.value}</td>
      <td>{value.freq}</td>
      <td>
        <progress max={total} value={value.freq}></progress>
      </td>
    </tr>
  )
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
        <tbody>{stats.map(v => val(v))}</tbody>
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
