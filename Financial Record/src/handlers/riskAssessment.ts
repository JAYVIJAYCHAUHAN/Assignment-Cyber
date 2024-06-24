export const assessRisk = (data: any): any => {
  const { amount, transactionDetails, userDetails } = data;

  let riskScore = 0;

  // Example criteria
  if (amount > 1000) riskScore += 50;
  if (transactionDetails.countryCode !== "US") riskScore += 20;
  // Add more criteria...

  return { riskScore };
};
