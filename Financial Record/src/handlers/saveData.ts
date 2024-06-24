import * as fs from "fs";
import * as path from "path";

export const saveData = async (data: any): Promise<void> => {
  const filePath = path.join(__dirname, "../../data/transactions.json");
  fs.writeFileSync(filePath, JSON.stringify(data, null, 2));
};
