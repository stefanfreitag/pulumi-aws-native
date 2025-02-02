// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Schema for AWS Config ConfigRule
 */
export class ConfigRule extends pulumi.CustomResource {
    /**
     * Get an existing ConfigRule resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ConfigRule {
        return new ConfigRule(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:configuration:ConfigRule';

    /**
     * Returns true if the given object is an instance of ConfigRule.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ConfigRule {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ConfigRule.__pulumiType;
    }

    /**
     * ARN generated for the AWS Config rule 
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * Compliance details of the Config rule
     */
    public readonly compliance!: pulumi.Output<outputs.configuration.ComplianceProperties | undefined>;
    /**
     * ID of the config rule
     */
    public /*out*/ readonly configRuleId!: pulumi.Output<string>;
    /**
     * Name for the AWS Config rule
     */
    public readonly configRuleName!: pulumi.Output<string | undefined>;
    /**
     * Description provided for the AWS Config rule
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * List of EvaluationModeConfiguration objects
     */
    public readonly evaluationModes!: pulumi.Output<outputs.configuration.ConfigRuleEvaluationModeConfiguration[] | undefined>;
    /**
     * JSON string passed the Lambda function
     */
    public readonly inputParameters!: pulumi.Output<string | undefined>;
    /**
     * Maximum frequency at which the rule has to be evaluated
     */
    public readonly maximumExecutionFrequency!: pulumi.Output<string | undefined>;
    /**
     * Scope to constrain which resources can trigger the AWS Config rule
     */
    public readonly scope!: pulumi.Output<outputs.configuration.ConfigRuleScope | undefined>;
    /**
     * Source of events for the AWS Config rule
     */
    public readonly source!: pulumi.Output<outputs.configuration.ConfigRuleSource>;

    /**
     * Create a ConfigRule resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ConfigRuleArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.source === undefined) && !opts.urn) {
                throw new Error("Missing required property 'source'");
            }
            resourceInputs["compliance"] = args ? args.compliance : undefined;
            resourceInputs["configRuleName"] = args ? args.configRuleName : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["evaluationModes"] = args ? args.evaluationModes : undefined;
            resourceInputs["inputParameters"] = args ? args.inputParameters : undefined;
            resourceInputs["maximumExecutionFrequency"] = args ? args.maximumExecutionFrequency : undefined;
            resourceInputs["scope"] = args ? args.scope : undefined;
            resourceInputs["source"] = args ? args.source : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["configRuleId"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["compliance"] = undefined /*out*/;
            resourceInputs["configRuleId"] = undefined /*out*/;
            resourceInputs["configRuleName"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["evaluationModes"] = undefined /*out*/;
            resourceInputs["inputParameters"] = undefined /*out*/;
            resourceInputs["maximumExecutionFrequency"] = undefined /*out*/;
            resourceInputs["scope"] = undefined /*out*/;
            resourceInputs["source"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["configRuleName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(ConfigRule.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ConfigRule resource.
 */
export interface ConfigRuleArgs {
    /**
     * Compliance details of the Config rule
     */
    compliance?: pulumi.Input<inputs.configuration.CompliancePropertiesArgs>;
    /**
     * Name for the AWS Config rule
     */
    configRuleName?: pulumi.Input<string>;
    /**
     * Description provided for the AWS Config rule
     */
    description?: pulumi.Input<string>;
    /**
     * List of EvaluationModeConfiguration objects
     */
    evaluationModes?: pulumi.Input<pulumi.Input<inputs.configuration.ConfigRuleEvaluationModeConfigurationArgs>[]>;
    /**
     * JSON string passed the Lambda function
     */
    inputParameters?: pulumi.Input<string>;
    /**
     * Maximum frequency at which the rule has to be evaluated
     */
    maximumExecutionFrequency?: pulumi.Input<string>;
    /**
     * Scope to constrain which resources can trigger the AWS Config rule
     */
    scope?: pulumi.Input<inputs.configuration.ConfigRuleScopeArgs>;
    /**
     * Source of events for the AWS Config rule
     */
    source: pulumi.Input<inputs.configuration.ConfigRuleSourceArgs>;
}
