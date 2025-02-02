// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::SecretsManager::Secret
 */
export function getSecret(args: GetSecretArgs, opts?: pulumi.InvokeOptions): Promise<GetSecretResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:secretsmanager:getSecret", {
        "id": args.id,
    }, opts);
}

export interface GetSecretArgs {
    /**
     * secret Id, the Arn of the resource.
     */
    id: string;
}

export interface GetSecretResult {
    /**
     * (Optional) Specifies a user-provided description of the secret.
     */
    readonly description?: string;
    /**
     * secret Id, the Arn of the resource.
     */
    readonly id?: string;
    /**
     * (Optional) Specifies the ARN, Key ID, or alias of the AWS KMS customer master key (CMK) used to encrypt the SecretString.
     */
    readonly kmsKeyId?: string;
    /**
     * (Optional) A list of ReplicaRegion objects. The ReplicaRegion type consists of a Region (required) and the KmsKeyId which can be an ARN, Key ID, or Alias.
     */
    readonly replicaRegions?: outputs.secretsmanager.SecretReplicaRegion[];
    /**
     * The list of user-defined tags associated with the secret. Use tags to manage your AWS resources. For additional information about tags, see TagResource.
     */
    readonly tags?: outputs.Tag[];
}
/**
 * Resource Type definition for AWS::SecretsManager::Secret
 */
export function getSecretOutput(args: GetSecretOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetSecretResult> {
    return pulumi.output(args).apply((a: any) => getSecret(a, opts))
}

export interface GetSecretOutputArgs {
    /**
     * secret Id, the Arn of the resource.
     */
    id: pulumi.Input<string>;
}
