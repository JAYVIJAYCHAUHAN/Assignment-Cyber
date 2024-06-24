import { createCipheriv, randomBytes, createHash, publicEncrypt } from "crypto";

// Mock implementation for the missing module
const publicKey = "YOUR_PUBLIC_KEY";

export const encryptData = (data: any): any => {
  const algorithm = "aes-256-ctr";
  const secretKey = randomBytes(32);
  const iv = randomBytes(16);

  const cipher = createCipheriv(algorithm, secretKey, iv);

  let encrypted = cipher.update(JSON.stringify(data), "utf8", "hex");
  encrypted += cipher.final("hex");

  const encryptedKey = publicEncrypt(publicKey, secretKey).toString("hex");

  return {
    iv: iv.toString("hex"),
    encryptedData: encrypted,
    encryptedKey: encryptedKey,
  };
};
