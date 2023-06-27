// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * A markup/discount that is defined for a specific set of services that can later be associated with a pricing plan.
 */
export function getPricingRule(args: GetPricingRuleArgs, opts?: pulumi.InvokeOptions): Promise<GetPricingRuleResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:billingconductor:getPricingRule", {
        "arn": args.arn,
    }, opts);
}

export interface GetPricingRuleArgs {
    /**
     * Pricing rule ARN
     */
    arn: string;
}

export interface GetPricingRuleResult {
    /**
     * Pricing rule ARN
     */
    readonly arn?: string;
    /**
     * The number of pricing plans associated with pricing rule
     */
    readonly associatedPricingPlanCount?: number;
    /**
     * Creation timestamp in UNIX epoch time format
     */
    readonly creationTime?: number;
    /**
     * Pricing rule description
     */
    readonly description?: string;
    /**
     * Latest modified timestamp in UNIX epoch time format
     */
    readonly lastModifiedTime?: number;
    /**
     * Pricing rule modifier percentage
     */
    readonly modifierPercentage?: number;
    /**
     * Pricing rule name
     */
    readonly name?: string;
    readonly tags?: outputs.billingconductor.PricingRuleTag[];
    /**
     * The set of tiering configurations for the pricing rule.
     */
    readonly tiering?: outputs.billingconductor.TieringProperties;
    /**
     * One of MARKUP, DISCOUNT or TIERING that describes the behaviour of the pricing rule.
     */
    readonly type?: enums.billingconductor.PricingRuleType;
}
/**
 * A markup/discount that is defined for a specific set of services that can later be associated with a pricing plan.
 */
export function getPricingRuleOutput(args: GetPricingRuleOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetPricingRuleResult> {
    return pulumi.output(args).apply((a: any) => getPricingRule(a, opts))
}

export interface GetPricingRuleOutputArgs {
    /**
     * Pricing rule ARN
     */
    arn: pulumi.Input<string>;
}
