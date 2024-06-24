import { createHash } from "crypto";

export const anonymizeData = (data: any): any => {
  const { userId, userDetails } = data;

  // Generate pseudonym
  const pseudonym = createHash("sha256").update(userId).digest("hex");

  // Anonymize user details
  const anonymizedDetails = {
    ...userDetails,
    firstName: "Anonymous",
    lastName: "User",
    email: pseudonym + "@example.com",
    phone: "000-000-0000",
  };

  return {
    ...data,
    userId: pseudonym,
    userDetails: anonymizedDetails,
  };
};
