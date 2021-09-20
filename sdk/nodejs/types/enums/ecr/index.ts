// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const RepositoryEncryptionType = {
    Aes256: "AES256",
    Kms: "KMS",
} as const;

/**
 * The encryption type to use.
 */
export type RepositoryEncryptionType = (typeof RepositoryEncryptionType)[keyof typeof RepositoryEncryptionType];

export const RepositoryImageTagMutability = {
    Mutable: "MUTABLE",
    Immutable: "IMMUTABLE",
} as const;

/**
 * The image tag mutability setting for the repository.
 */
export type RepositoryImageTagMutability = (typeof RepositoryImageTagMutability)[keyof typeof RepositoryImageTagMutability];
