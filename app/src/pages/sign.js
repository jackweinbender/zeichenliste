import React from "react"
// import { Link } from "gatsby"
import Layout from "../components/layout"
// import Image from "../components/image"
// import SEO from "../components/seo"
import BarChart from "../components/bar-chart"

const SignPage = () => {
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
  return (
    <Layout>
      {/* <SEO title="Home" /> */}
      <div className="results-card">
        <h3 className="results-card-header">
          <a href="/signs/495">É</a>
        </h3>
        <div className="results-card-sign">
          <span className="cuneiform">𒂍</span>
        </div>
        <div className="results-card-values">
          <span className="value">ʾa3</span>
          <span className="value">aʾ3</span>
          <span className="value">a14</span>
          <span className="value">bītu</span>
          <span className="value">bed</span>
          <span className="value">bet</span>
          <span className="value">betu</span>
          <span className="value">bid</span>
          <span className="value">bit</span>
          <span className="value">biti</span>
          <span className="value">bitu</span>
          <span className="value">biṭ</span>
          <span className="value">e2</span>
          <span className="value">eʾ3</span>
          <span className="value">iski</span>
          <span className="value">pet</span>
          <span className="value">pid</span>
          <span className="value">pit</span>
          <span className="value">piṭ</span>
        </div>
        <div className="results-card-list-ids">
          <span className="signlist-id-badge">Borger: 495</span>
          <span className="signlist-id-badge">Labat: 324</span>
          <span className="signlist-id-badge">Huehnergard: 78</span>
          <span className="signlist-id-badge">Deimel: 324</span>
          <span className="signlist-id-badge">Mittermayer: 107</span>
          <span className="signlist-id-badge">Heth ZL: 199</span>
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
    </Layout>
  )
}
export default SignPage
