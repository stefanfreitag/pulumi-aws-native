// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::SSM::Document resource is an SSM document in AWS Systems Manager that defines the actions that Systems Manager performs, which can be used to set up and run commands on your instances.
 */
export function getDocument(args: GetDocumentArgs, opts?: pulumi.InvokeOptions): Promise<GetDocumentResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:ssm:getDocument", {
        "name": args.name,
    }, opts);
}

export interface GetDocumentArgs {
    /**
     * A name for the Systems Manager document.
     */
    name: string;
}

export interface GetDocumentResult {
    /**
     * The content for the Systems Manager document in JSON, YAML or String format.
     */
    readonly content?: any;
    /**
     * Specify the document format for the request. The document format can be either JSON or YAML. JSON is the default format.
     */
    readonly documentFormat?: enums.ssm.DocumentFormat;
    /**
     * A list of SSM documents required by a document. For example, an ApplicationConfiguration document requires an ApplicationConfigurationSchema document.
     */
    readonly requires?: outputs.ssm.DocumentRequires[];
    /**
     * Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment.
     */
    readonly tags?: outputs.ssm.DocumentTag[];
    /**
     * Specify a target type to define the kinds of resources the document can run on.
     */
    readonly targetType?: string;
    /**
     * An optional field specifying the version of the artifact you are creating with the document. This value is unique across all versions of a document, and cannot be changed.
     */
    readonly versionName?: string;
}
/**
 * The AWS::SSM::Document resource is an SSM document in AWS Systems Manager that defines the actions that Systems Manager performs, which can be used to set up and run commands on your instances.
 */
export function getDocumentOutput(args: GetDocumentOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDocumentResult> {
    return pulumi.output(args).apply((a: any) => getDocument(a, opts))
}

export interface GetDocumentOutputArgs {
    /**
     * A name for the Systems Manager document.
     */
    name: pulumi.Input<string>;
}
