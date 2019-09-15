// import { Link } from "gatsby"
import PropTypes from "prop-types"
import React from "react"

const Header = ({ siteTitle }) => (
  <form className="search-box" action="/" method="GET">
    <input type="text" name="search" />
    <button type="submit">Search&nbsp;»</button>
  </form>
)

Header.propTypes = {
  siteTitle: PropTypes.string,
}

Header.defaultProps = {
  siteTitle: ``,
}

export default Header
