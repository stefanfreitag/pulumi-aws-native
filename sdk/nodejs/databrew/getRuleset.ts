// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::DataBrew::Ruleset.
 */
export function getRuleset(args: GetRulesetArgs, opts?: pulumi.InvokeOptions): Promise<GetRulesetResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:databrew:getRuleset", {
        "name": args.name,
    }, opts);
}

export interface GetRulesetArgs {
    /**
     * Name of the Ruleset
     */
    name: string;
}

export interface GetRulesetResult {
    /**
     * Description of the Ruleset
     */
    readonly description?: string;
    /**
     * List of the data quality rules in the ruleset
     */
    readonly rules?: outputs.databrew.RulesetRule[];
    readonly tags?: outputs.Tag[];
}
/**
 * Resource schema for AWS::DataBrew::Ruleset.
 */
export function getRulesetOutput(args: GetRulesetOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetRulesetResult> {
    return pulumi.output(args).apply((a: any) => getRuleset(a, opts))
}

export interface GetRulesetOutputArgs {
    /**
     * Name of the Ruleset
     */
    name: pulumi.Input<string>;
}
