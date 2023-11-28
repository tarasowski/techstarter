import { DynamoDBClient, GetItemCommand } from "@aws-sdk/client-dynamodb"

const client = new DynamoDBClient({ region: "us-east-1" })

export const handler = async (event) => {
  
  const body = event?.body
  const method = event?.httpMethod
  
  if (method === "GET") {
  
    const input = {
      TableName: "TechstarterTest",
      Key: {
        id: {"S": "0001"}
      }
    }
    const command = new GetItemCommand(input)
    const response = await client.send(command)
    const item = response.Item

    
    const responseToClient = {
      statusCode: 200,
      body: JSON.stringify(item),
    };
    return responseToClient
  }
  
  const error = {
    statusCode: 500,
    body: JSON.stringify("Something went wrong. Wrong http method, please use GET or POST")
  }
  
  return error
  
};

