export const validateData = (data: any): void => {
  const requiredFields = [
    "transactionId",
    "userId",
    "transactionDetails",
    "userDetails",
  ];

  requiredFields.forEach((field) => {
    if (!data[field]) {
      throw new Error(`Missing required field: ${field}`);
    }
  });
};
