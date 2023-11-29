// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { BucketPolicyArgs } from "./bucketPolicy";
export type BucketPolicy = import("./bucketPolicy").BucketPolicy;
export const BucketPolicy: typeof import("./bucketPolicy").BucketPolicy = null as any;
utilities.lazyLoad(exports, ["BucketPolicy"], () => require("./bucketPolicy"));

export { DirectoryBucketArgs } from "./directoryBucket";
export type DirectoryBucket = import("./directoryBucket").DirectoryBucket;
export const DirectoryBucket: typeof import("./directoryBucket").DirectoryBucket = null as any;
utilities.lazyLoad(exports, ["DirectoryBucket"], () => require("./directoryBucket"));

export { GetBucketPolicyArgs, GetBucketPolicyResult, GetBucketPolicyOutputArgs } from "./getBucketPolicy";
export const getBucketPolicy: typeof import("./getBucketPolicy").getBucketPolicy = null as any;
export const getBucketPolicyOutput: typeof import("./getBucketPolicy").getBucketPolicyOutput = null as any;
utilities.lazyLoad(exports, ["getBucketPolicy","getBucketPolicyOutput"], () => require("./getBucketPolicy"));

export { GetDirectoryBucketArgs, GetDirectoryBucketResult, GetDirectoryBucketOutputArgs } from "./getDirectoryBucket";
export const getDirectoryBucket: typeof import("./getDirectoryBucket").getDirectoryBucket = null as any;
export const getDirectoryBucketOutput: typeof import("./getDirectoryBucket").getDirectoryBucketOutput = null as any;
utilities.lazyLoad(exports, ["getDirectoryBucket","getDirectoryBucketOutput"], () => require("./getDirectoryBucket"));


// Export enums:
export * from "../types/enums/s3express";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:s3express:BucketPolicy":
                return new BucketPolicy(name, <any>undefined, { urn })
            case "aws-native:s3express:DirectoryBucket":
                return new DirectoryBucket(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "s3express", _module)
