// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Definition of AWS::RedshiftServerless::Namespace Resource Type
 */
export function getNamespace(args: GetNamespaceArgs, opts?: pulumi.InvokeOptions): Promise<GetNamespaceResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:redshiftserverless:getNamespace", {
        "namespaceName": args.namespaceName,
    }, opts);
}

export interface GetNamespaceArgs {
    /**
     * A unique identifier for the namespace. You use this identifier to refer to the namespace for any subsequent namespace operations such as deleting or modifying. All alphabetical characters must be lower case. Namespace name should be unique for all namespaces within an AWS account.
     */
    namespaceName: string;
}

export interface GetNamespaceResult {
    /**
     * The user name associated with the admin user for the namespace that is being created. Only alphanumeric characters and underscores are allowed. It should start with an alphabet.
     */
    readonly adminUsername?: string;
    /**
     * The database name associated for the namespace that is being created. Only alphanumeric characters and underscores are allowed. It should start with an alphabet.
     */
    readonly dbName?: string;
    /**
     * The default IAM role ARN for the namespace that is being created.
     */
    readonly defaultIamRoleArn?: string;
    /**
     * A list of AWS Identity and Access Management (IAM) roles that can be used by the namespace to access other AWS services. You must supply the IAM roles in their Amazon Resource Name (ARN) format. The Default role limit for each request is 10.
     */
    readonly iamRoles?: string[];
    /**
     * The AWS Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the namespace.
     */
    readonly kmsKeyId?: string;
    /**
     * The collection of log types to be exported provided by the customer. Should only be one of the three supported log types: userlog, useractivitylog and connectionlog
     */
    readonly logExports?: enums.redshiftserverless.NamespaceLogExport[];
    readonly namespace?: outputs.redshiftserverless.Namespace;
}
/**
 * Definition of AWS::RedshiftServerless::Namespace Resource Type
 */
export function getNamespaceOutput(args: GetNamespaceOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetNamespaceResult> {
    return pulumi.output(args).apply((a: any) => getNamespace(a, opts))
}

export interface GetNamespaceOutputArgs {
    /**
     * A unique identifier for the namespace. You use this identifier to refer to the namespace for any subsequent namespace operations such as deleting or modifying. All alphabetical characters must be lower case. Namespace name should be unique for all namespaces within an AWS account.
     */
    namespaceName: pulumi.Input<string>;
}
