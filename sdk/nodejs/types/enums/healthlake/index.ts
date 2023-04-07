// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const FHIRDatastoreDatastoreStatus = {
    Creating: "CREATING",
    Active: "ACTIVE",
    Deleting: "DELETING",
    Deleted: "DELETED",
} as const;

/**
 * The status of the Data Store. Possible statuses are 'CREATING', 'ACTIVE', 'DELETING', or 'DELETED'.
 */
export type FHIRDatastoreDatastoreStatus = (typeof FHIRDatastoreDatastoreStatus)[keyof typeof FHIRDatastoreDatastoreStatus];

export const FHIRDatastoreDatastoreTypeVersion = {
    R4: "R4",
} as const;

/**
 * The FHIR version. Only R4 version data is supported.
 */
export type FHIRDatastoreDatastoreTypeVersion = (typeof FHIRDatastoreDatastoreTypeVersion)[keyof typeof FHIRDatastoreDatastoreTypeVersion];

export const FHIRDatastoreKmsEncryptionConfigCmkType = {
    CustomerManagedKmsKey: "CUSTOMER_MANAGED_KMS_KEY",
    AwsOwnedKmsKey: "AWS_OWNED_KMS_KEY",
} as const;

/**
 * The type of customer-managed-key (CMK) used for encryption. The two types of supported CMKs are customer owned CMKs and AWS owned CMKs.
 */
export type FHIRDatastoreKmsEncryptionConfigCmkType = (typeof FHIRDatastoreKmsEncryptionConfigCmkType)[keyof typeof FHIRDatastoreKmsEncryptionConfigCmkType];

export const FHIRDatastorePreloadDataConfigPreloadDataType = {
    Synthea: "SYNTHEA",
} as const;

/**
 * The type of preloaded data. Only Synthea preloaded data is supported.
 */
export type FHIRDatastorePreloadDataConfigPreloadDataType = (typeof FHIRDatastorePreloadDataConfigPreloadDataType)[keyof typeof FHIRDatastorePreloadDataConfigPreloadDataType];
