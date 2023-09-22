// skd software developerment kit -> we can communicate with the AWS services
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient, PutCommand, ScanCommand } from "@aws-sdk/lib-dynamodb";

const tableName = "MyTodo"

// we need a client to connect to the database!!!! 👇
const client = new DynamoDBClient({});
const docClient = DynamoDBDocumentClient.from(client);

async function scanItems(tableName) {
  const command = new ScanCommand({TableName: tableName});
    const response = await docClient.send(command)  
    return response.Items // -> Items[{id, taskName}, {id, taskName}]
} // -> returns a Promise

async function putItem(item /* {id, taskName} */) {
  const command = new PutCommand({
    TableName: tableName,
    Item: {
      id: item.id,
      taskName: item.taskName
    },
  })
  const response = await docClient.send(command)
  return response
} // -> returns a Promise

 const response = {
    statusCode: 200,
    headers: {
      "Access-Control-Allow-Origin": "*",
    },
    body: JSON.stringify('Wir haben dein Todo hinzugefügt! 🚀'),
  };
  
const error = {
  statusCode: 500,
  headers: {
      "Access-Control-Allow-Origin": "*",
    },
    body: JSON.stringify('Hey! Da war ein Fehler, bitte Admin kontaktieren 🆘'),
}

// express is req in lambda it is called event
export const handler = async (event) => {
  
  const method = event.requestContext.http.method
  
  try {
    if (method === "POST") {
      const body = event.body
      const item = JSON.parse(body)
      await putItem(item)
      return response
    } else if (method === "GET") {
      const items = await scanItems("MyTodo")
      return {
        statusCode: 200,
        headers: {
          "Access-Control-Allow-Origin": "*", // put this to fix the CORS error
        },
        body: JSON.stringify(items)
      }
    }
  } catch(e) {
    console.log(e)
    return error
  }

};

