import React from "react"
import { Link } from "gatsby"

import Layout from "../components/layout"
import Image from "../components/image"
import SEO from "../components/seo"

const IndexPage = () => (
  <Layout>
    <SEO title="Home" />
    <div class="search-instructions">
      <h3>Search Instructions</h3>
      <p>
        Search for sign name, reading, or sign number in the following sign
        lists:
      </p>
      <ul>
        <li>
          Borger's <i>Zeichenlexikon, 2nd ed.</i>
        </li>
        <li>
          Labat's <i>Manuel</i> (= Snell's <i>Workbook</i>)
        </li>
        <li>
          Deimel's <i>Lexikon</i>
        </li>
        <li>
          Rüster and Neu's <i>Hethitisches Zeichenlexikon</i>
        </li>
        <li>
          Mittermayer's <i>Zeichenliste</i>
        </li>
        <li>
          Huehnergard's <i>Grammar, 3rd ed.</i>
        </li>
      </ul>
      <p>You can use accents or numbers, e.g., bé/be2, šà/ša3.</p>
      <p>
        Values that have not yet been assigned a number appear as x, e.g.,
        subarrumx as a reading of the ARAD sign.
      </p>
      <p>
        The following special characters can be used: ḫ/h - š/sz - ĝ/ŋ/ng - ṣ/s,
        - ṭ/t
      </p>
      <h3>Example Searches:</h3>
      <dl>
        <dt>e</dt>
        <dd>Returns all "E" signs (E, É, KA [=E7], etc.)</dd>
        <dt>e2</dt>
        <dd>Returns only É (E2)</dd>
      </dl>
    </div>
  </Layout>
)

export default IndexPage
