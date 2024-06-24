import { APIGatewayProxyHandler } from "aws-lambda";
import { anonymizeData } from "./handlers/anonymize";
import { encryptData } from "./handlers/encrypt";
import { assessRisk } from "./handlers/riskAssessment";
import { saveData } from "./handlers/saveData";

export const processTransaction = async (
  event,
  _context
) => {
  try {
    const body = JSON.parse(event.body);

    // Validate the data
    validateData(body);

    // Anonymize the data
    const anonymizedData = anonymizeData(body);

    // Encrypt the data
    const encryptedData = encryptData(anonymizedData);

    // Assess risk
    const riskData = assessRisk(body);

    // Save data
    await saveData({ ...encryptedData, riskData });

    return {
      statusCode: 200,
      body: JSON.stringify({ message: "Transaction processed successfully" }),
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({
        message: "Internal Server Error",
        error: error.message,
      }),
    };
  }
};
