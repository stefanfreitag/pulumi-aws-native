// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::AccessAnalyzer::Analyzer type specifies an analyzer of the user's account
 */
export function getAnalyzer(args: GetAnalyzerArgs, opts?: pulumi.InvokeOptions): Promise<GetAnalyzerResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:accessanalyzer:getAnalyzer", {
        "arn": args.arn,
    }, opts);
}

export interface GetAnalyzerArgs {
    /**
     * Amazon Resource Name (ARN) of the analyzer
     */
    arn: string;
}

export interface GetAnalyzerResult {
    readonly archiveRules?: outputs.accessanalyzer.AnalyzerArchiveRule[];
    /**
     * Amazon Resource Name (ARN) of the analyzer
     */
    readonly arn?: string;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    readonly tags?: outputs.Tag[];
}
/**
 * The AWS::AccessAnalyzer::Analyzer type specifies an analyzer of the user's account
 */
export function getAnalyzerOutput(args: GetAnalyzerOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetAnalyzerResult> {
    return pulumi.output(args).apply((a: any) => getAnalyzer(a, opts))
}

export interface GetAnalyzerOutputArgs {
    /**
     * Amazon Resource Name (ARN) of the analyzer
     */
    arn: pulumi.Input<string>;
}
