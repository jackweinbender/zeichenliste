import React from "react"

export default ({ signlist, list_id }) => {
  if (!list_id) {
    return <></>
  }
  return (
    <span className="signlist-id-badge">
      {signlist}: {list_id}
    </span>
  )
}
