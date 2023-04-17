/** @type {import('ts-jest').JestConfigWithTsJest} */
module.exports = {
    verbose: true,
    collectCoverage: true,
    testEnvironment: 'node',
    testTimeout: 10000,
    maxWorkers:3,
    testRegex: '/test/.*\\.(test|spec)?\\.(js)$',
    moduleFileExtensions: ['ts', 'tsx', 'js', 'jsx', 'json', 'node'],
    "testPathIgnorePatterns": [
        // "<rootDir>/test/eth/",
        // "<rootDir>/test/klay/account",
        // "<rootDir>/test/klay/configuration",
        // "<rootDir>/test/klay/transaction",
        //"<rootDir>/test/klay/block"
    ]
};
