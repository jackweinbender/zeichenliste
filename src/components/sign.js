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
    ob: [
      {
        freq: "215",
        type: "Logogram",
        value: "E2",
      },
    ],
    nb: [
      {
        freq: "14",
        type: "Syllabogram",
        value: "pit",
      },
      {
        freq: "46",
        type: "Syllabogram",
        value: "bit",
      },
      {
        freq: "2",
        type: "Syllabogram",
        value: "e2",
      },
      {
        freq: "6",
        type: "Syllabogram",
        value: "bet",
      },
      {
        freq: "2",
        type: "Syllabogram",
        value: "pet",
      },
      {
        freq: "26",
        type: "Determinative",
        value: "E2",
      },
    ],
    na: [
      {
        freq: "20",
        type: "Syllabogram",
        value: "pit",
      },
      {
        freq: "122",
        type: "Syllabogram",
        value: "bit",
      },
      {
        freq: "14",
        type: "Syllabogram",
        value: "pet",
      },
      {
        freq: "4",
        type: "Syllabogram",
        value: "e2",
      },
      {
        freq: "2",
        type: "Syllabogram",
        value: "bid",
      },
      {
        freq: "4",
        type: "Syllabogram",
        value: "bet",
      },
      {
        freq: "34",
        type: "Determinative",
        value: "E2",
      },
    ],
    ebla: [
      {
        freq: "6400",
        type: "Syllabogram",
        value: "ʾa3",
      },
      {
        freq: "115",
        type: "undefined",
        value: "E2",
      },
      {
        freq: "6",
        type: "Logogram",
        value: "ʾA3",
      },
      {
        freq: "3",
        type: "Syllabogram",
        value: "e2",
      },
    ],
    oakk: [
      {
        freq: 1,
        type: "Syllabogram",
        value: "bit",
      },
      {
        freq: 1,
        type: "Syllabogram",
        value: "e2",
      },
    ],
  }
  const total = array =>
    array.reduce((acc, next) => {
      return acc + parseInt(next.freq)
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
  }
`
