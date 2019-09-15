const path = require(`path`)
exports.createPages = ({ graphql, actions }) => {
  const { createPage } = actions
  return graphql(`
    {
      allSignsJson {
        edges {
          node {
            borger_id
          }
        }
      }
    }
  `).then(result => {
    result.data.allSignsJson.edges.forEach(({ node }) => {
      createPage({
        path: `signs/${node.borger_id}`,
        component: path.resolve(`./src/components/sign.js`),
        context: { borger_id: node.borger_id },
      })
    })
  })
}
// exports.createSchemaCustomization = ({ actions }) => {
//   const { createTypes } = actions
//   const typeDefs = `
//     type LettersJson implements Node {
//       sort: Int
//       language: String,
//       char: String,
//       translit: String,
//       name: String,
//       roots: [RootsJson] @link(by: "letter", from: "sort")
//     }
//   `
//   createTypes(typeDefs)
// }
