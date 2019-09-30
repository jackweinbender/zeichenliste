import React from "react"
// import { Link } from "gatsby"
import Layout from "./layout"
import { graphql } from "gatsby"
// import Image from "../components/image"
// import SEO from "../components/seo"
import BarChart from "./bar-chart"
import SignlistIdBadge from "./signlist_id_badge"

const SignPage = ({ data }) => {
  const stats = {
    ob: data.freq_ob.edges,
    nb: data.freq_nb.edges,
    na: data.freq_na.edges,
    ebla: data.freq_ebla.edges,
    oakk: data.freq_oakk.edges,
  }
  const total = array =>
    array.reduce((acc, {node}) => {
      return acc + parseInt(node.freq)
    }, 0)
  const sign_value = value => {
    return <span className="value">{value}</span>
  }
  return (
    <Layout>
      {/* <SEO title="Home" /> */}
      <div className="results-card">
        <h3 className="results-card-header">
          <a href={`/signs/${data.sign.borger_id}`}>{data.sign.borger_name}</a>
        </h3>
        <div className="results-card-sign">
          <span className="cuneiform">{data.sign.unicode_value}</span>
        </div>
        <div className="results-card-values">
          {data.sign.values.map(v => sign_value(v))}
        </div>
        <div className="results-card-list-ids">
          <SignlistIdBadge signlist="Borger" list_id={data.sign.borger_id} />
          <SignlistIdBadge signlist="Labat" list_id={data.sign.labat_id} />
          <SignlistIdBadge
            signlist="Heuhnergard"
            list_id={data.sign.huehnergard_id}
          />
          <SignlistIdBadge signlist="Deimel" list_id={data.sign.deimel_id} />
          <SignlistIdBadge
            signlist="Mittermeyer"
            list_id={data.sign.mittermayer_id}
          />
          <SignlistIdBadge signlist="Heth Zl" list_id={data.sign.hethzl_id} />
        </div>
      </div>
      <div className="stats">
        <h2 className="title">Distribution by Corpus</h2>
        <div className="stats-row">
          <BarChart
            title="Old Babylonian"
            stats={stats["ob"]}
            total={total(stats["ob"])}
          />
          <BarChart
            title="Neo-Bablylonian"
            stats={stats["nb"]}
            total={total(stats["nb"])}
          />
        </div>
        <div className="stats-row">
          <BarChart
            title="Neo-Assyrian"
            stats={stats["na"]}
            total={total(stats["na"])}
          />
          <BarChart
            title="Ebla"
            stats={stats["ebla"]}
            total={total(stats["ebla"])}
          />
          <BarChart
            title="Old Akkadian"
            stats={stats["oakk"]}
            total={total(stats["oakk"])}
          />
        </div>
      </div>
      {/* Debugging */}
      <hr />
      <h3>Debug Data (sign.js)</h3>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </Layout>
  )
}
export default SignPage

export const query = graphql`
  query Page($borger_id: Int) {
    sign: signsJson(borger_id: { eq: $borger_id }) {
      borger_name
      oracc_name
      unicode_value
      values
      borger_id
      labat_id
      huehnergard_id
      mittermayer_id
      hethzl_id
      deimel_id
    }
    freq_ob: allFreqObJson(filter: { borger_id: { eq: $borger_id } }) {
      edges {
        node {
          id
          freq
          type
          value
          corpus
          borger_id
        }
      }
    }
    freq_na: allFreqNaJson(filter: { borger_id: { eq: $borger_id } }) {
      edges {
        node {
          id
          freq
          type
          value
          corpus
          borger_id
        }
      }
    }
    freq_nb: allFreqNbJson(filter: { borger_id: { eq: $borger_id } }) {
      edges {
        node {
          id
          freq
          type
          value
          corpus
          borger_id
        }
      }
    }
    freq_oakk: allFreqOakkJson(filter: { borger_id: { eq: $borger_id } }) {
      edges {
        node {
          id
          freq
          type
          value
          corpus
          borger_id
        }
      }
    }
    freq_ebla: allFreqEblaJson(filter: { borger_id: { eq: $borger_id } }) {
      edges {
        node {
          id
          freq
          type
          value
          corpus
          borger_id
        }
      }
    }
  }
`
