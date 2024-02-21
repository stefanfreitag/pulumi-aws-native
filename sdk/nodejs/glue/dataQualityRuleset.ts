// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Glue::DataQualityRuleset
 *
 * @deprecated DataQualityRuleset is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class DataQualityRuleset extends pulumi.CustomResource {
    /**
     * Get an existing DataQualityRuleset resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): DataQualityRuleset {
        pulumi.log.warn("DataQualityRuleset is deprecated: DataQualityRuleset is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new DataQualityRuleset(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:glue:DataQualityRuleset';

    /**
     * Returns true if the given object is an instance of DataQualityRuleset.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DataQualityRuleset {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DataQualityRuleset.__pulumiType;
    }

    public readonly clientToken!: pulumi.Output<string | undefined>;
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly name!: pulumi.Output<string | undefined>;
    public readonly ruleset!: pulumi.Output<string | undefined>;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Glue::DataQualityRuleset` for more information about the expected schema for this property.
     */
    public readonly tags!: pulumi.Output<any | undefined>;
    public readonly targetTable!: pulumi.Output<outputs.glue.DataQualityRulesetDataQualityTargetTable | undefined>;

    /**
     * Create a DataQualityRuleset resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated DataQualityRuleset is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args?: DataQualityRulesetArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("DataQualityRuleset is deprecated: DataQualityRuleset is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["clientToken"] = args ? args.clientToken : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["ruleset"] = args ? args.ruleset : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["targetTable"] = args ? args.targetTable : undefined;
        } else {
            resourceInputs["clientToken"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["ruleset"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["targetTable"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(DataQualityRuleset.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a DataQualityRuleset resource.
 */
export interface DataQualityRulesetArgs {
    clientToken?: pulumi.Input<string>;
    description?: pulumi.Input<string>;
    name?: pulumi.Input<string>;
    ruleset?: pulumi.Input<string>;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Glue::DataQualityRuleset` for more information about the expected schema for this property.
     */
    tags?: any;
    targetTable?: pulumi.Input<inputs.glue.DataQualityRulesetDataQualityTargetTableArgs>;
}
