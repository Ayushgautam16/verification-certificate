const Web3 = require('web3');
const contractABI = [ /* ABI from Solidity Contract */ ];
const contractAddress = '0xYourContractAddressHere';
const web3 = new Web3('https://mainnet.infura.io/v3/your-infura-key');

const contract = new web3.eth.Contract(contractABI, contractAddress);

const issueCertificate = async (issuer, recipient, documentHash) => {
    const accounts = await web3.eth.getAccounts();
    const receipt = await contract.methods.issueCertificate(issuer, recipient, documentHash)
        .send({ from: accounts[0] });
    console.log('Certificate issued:', receipt);
};

const verifyCertificate = async (certificateId) => {
    const certificate = await contract.methods.verifyCertificate(certificateId).call();
    console.log('Certificate details:', certificate);
};

// Example of issuing a certificate
issueCertificate('University of Example', 'John Doe', 'QmTzQ1Yc7...'); // Replace with actual IPFS hash or document hash

// Example of verifying a certificate
verifyCertificate(1);

