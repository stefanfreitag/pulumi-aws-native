// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * A markup/discount that is defined for a specific set of services that can later be associated with a pricing plan.
 *
 * @deprecated PricingRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class PricingRule extends pulumi.CustomResource {
    /**
     * Get an existing PricingRule resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): PricingRule {
        pulumi.log.warn("PricingRule is deprecated: PricingRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new PricingRule(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:billingconductor:PricingRule';

    /**
     * Returns true if the given object is an instance of PricingRule.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PricingRule {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PricingRule.__pulumiType;
    }

    /**
     * Pricing rule ARN
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The number of pricing plans associated with pricing rule
     */
    public /*out*/ readonly associatedPricingPlanCount!: pulumi.Output<number>;
    /**
     * The seller of services provided by AWS, their affiliates, or third-party providers selling services via AWS Marketplaces. Supported billing entities are AWS, AWS Marketplace, and AISPL.
     */
    public readonly billingEntity!: pulumi.Output<enums.billingconductor.PricingRuleBillingEntity | undefined>;
    /**
     * Creation timestamp in UNIX epoch time format
     */
    public /*out*/ readonly creationTime!: pulumi.Output<number>;
    /**
     * Pricing rule description
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Latest modified timestamp in UNIX epoch time format
     */
    public /*out*/ readonly lastModifiedTime!: pulumi.Output<number>;
    /**
     * Pricing rule modifier percentage
     */
    public readonly modifierPercentage!: pulumi.Output<number | undefined>;
    /**
     * Pricing rule name
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The Operation which a SKU pricing rule is modifying
     */
    public readonly operation!: pulumi.Output<string | undefined>;
    /**
     * A term used to categorize the granularity of a Pricing Rule.
     */
    public readonly scope!: pulumi.Output<enums.billingconductor.PricingRuleScope>;
    /**
     * The service which a pricing rule is applied on
     */
    public readonly service!: pulumi.Output<string | undefined>;
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;
    /**
     * The set of tiering configurations for the pricing rule.
     */
    public readonly tiering!: pulumi.Output<outputs.billingconductor.TieringProperties | undefined>;
    /**
     * One of MARKUP, DISCOUNT or TIERING that describes the behaviour of the pricing rule.
     */
    public readonly type!: pulumi.Output<enums.billingconductor.PricingRuleType>;
    /**
     * The UsageType which a SKU pricing rule is modifying
     */
    public readonly usageType!: pulumi.Output<string | undefined>;

    /**
     * Create a PricingRule resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated PricingRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: PricingRuleArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("PricingRule is deprecated: PricingRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.scope === undefined) && !opts.urn) {
                throw new Error("Missing required property 'scope'");
            }
            if ((!args || args.type === undefined) && !opts.urn) {
                throw new Error("Missing required property 'type'");
            }
            resourceInputs["billingEntity"] = args ? args.billingEntity : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["modifierPercentage"] = args ? args.modifierPercentage : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["operation"] = args ? args.operation : undefined;
            resourceInputs["scope"] = args ? args.scope : undefined;
            resourceInputs["service"] = args ? args.service : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["tiering"] = args ? args.tiering : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
            resourceInputs["usageType"] = args ? args.usageType : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["associatedPricingPlanCount"] = undefined /*out*/;
            resourceInputs["creationTime"] = undefined /*out*/;
            resourceInputs["lastModifiedTime"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["associatedPricingPlanCount"] = undefined /*out*/;
            resourceInputs["billingEntity"] = undefined /*out*/;
            resourceInputs["creationTime"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["lastModifiedTime"] = undefined /*out*/;
            resourceInputs["modifierPercentage"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["operation"] = undefined /*out*/;
            resourceInputs["scope"] = undefined /*out*/;
            resourceInputs["service"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["tiering"] = undefined /*out*/;
            resourceInputs["type"] = undefined /*out*/;
            resourceInputs["usageType"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["billingEntity", "operation", "scope", "service", "usageType"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(PricingRule.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a PricingRule resource.
 */
export interface PricingRuleArgs {
    /**
     * The seller of services provided by AWS, their affiliates, or third-party providers selling services via AWS Marketplaces. Supported billing entities are AWS, AWS Marketplace, and AISPL.
     */
    billingEntity?: pulumi.Input<enums.billingconductor.PricingRuleBillingEntity>;
    /**
     * Pricing rule description
     */
    description?: pulumi.Input<string>;
    /**
     * Pricing rule modifier percentage
     */
    modifierPercentage?: pulumi.Input<number>;
    /**
     * Pricing rule name
     */
    name?: pulumi.Input<string>;
    /**
     * The Operation which a SKU pricing rule is modifying
     */
    operation?: pulumi.Input<string>;
    /**
     * A term used to categorize the granularity of a Pricing Rule.
     */
    scope: pulumi.Input<enums.billingconductor.PricingRuleScope>;
    /**
     * The service which a pricing rule is applied on
     */
    service?: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
    /**
     * The set of tiering configurations for the pricing rule.
     */
    tiering?: pulumi.Input<inputs.billingconductor.TieringPropertiesArgs>;
    /**
     * One of MARKUP, DISCOUNT or TIERING that describes the behaviour of the pricing rule.
     */
    type: pulumi.Input<enums.billingconductor.PricingRuleType>;
    /**
     * The UsageType which a SKU pricing rule is modifying
     */
    usageType?: pulumi.Input<string>;
}
