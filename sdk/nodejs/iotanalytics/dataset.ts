// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::IoTAnalytics::Dataset
 */
export class Dataset extends pulumi.CustomResource {
    /**
     * Get an existing Dataset resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Dataset {
        return new Dataset(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:iotanalytics:Dataset';

    /**
     * Returns true if the given object is an instance of Dataset.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Dataset {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Dataset.__pulumiType;
    }

    public readonly actions!: pulumi.Output<outputs.iotanalytics.DatasetAction[]>;
    public readonly contentDeliveryRules!: pulumi.Output<outputs.iotanalytics.DatasetContentDeliveryRule[] | undefined>;
    public readonly datasetName!: pulumi.Output<string | undefined>;
    public readonly lateDataRules!: pulumi.Output<outputs.iotanalytics.DatasetLateDataRule[] | undefined>;
    public readonly retentionPeriod!: pulumi.Output<outputs.iotanalytics.DatasetRetentionPeriod | undefined>;
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;
    public readonly triggers!: pulumi.Output<outputs.iotanalytics.DatasetTrigger[] | undefined>;
    public readonly versioningConfiguration!: pulumi.Output<outputs.iotanalytics.DatasetVersioningConfiguration | undefined>;

    /**
     * Create a Dataset resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DatasetArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.actions === undefined) && !opts.urn) {
                throw new Error("Missing required property 'actions'");
            }
            resourceInputs["actions"] = args ? args.actions : undefined;
            resourceInputs["contentDeliveryRules"] = args ? args.contentDeliveryRules : undefined;
            resourceInputs["datasetName"] = args ? args.datasetName : undefined;
            resourceInputs["lateDataRules"] = args ? args.lateDataRules : undefined;
            resourceInputs["retentionPeriod"] = args ? args.retentionPeriod : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["triggers"] = args ? args.triggers : undefined;
            resourceInputs["versioningConfiguration"] = args ? args.versioningConfiguration : undefined;
        } else {
            resourceInputs["actions"] = undefined /*out*/;
            resourceInputs["contentDeliveryRules"] = undefined /*out*/;
            resourceInputs["datasetName"] = undefined /*out*/;
            resourceInputs["lateDataRules"] = undefined /*out*/;
            resourceInputs["retentionPeriod"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["triggers"] = undefined /*out*/;
            resourceInputs["versioningConfiguration"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["datasetName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Dataset.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Dataset resource.
 */
export interface DatasetArgs {
    actions: pulumi.Input<pulumi.Input<inputs.iotanalytics.DatasetActionArgs>[]>;
    contentDeliveryRules?: pulumi.Input<pulumi.Input<inputs.iotanalytics.DatasetContentDeliveryRuleArgs>[]>;
    datasetName?: pulumi.Input<string>;
    lateDataRules?: pulumi.Input<pulumi.Input<inputs.iotanalytics.DatasetLateDataRuleArgs>[]>;
    retentionPeriod?: pulumi.Input<inputs.iotanalytics.DatasetRetentionPeriodArgs>;
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
    triggers?: pulumi.Input<pulumi.Input<inputs.iotanalytics.DatasetTriggerArgs>[]>;
    versioningConfiguration?: pulumi.Input<inputs.iotanalytics.DatasetVersioningConfigurationArgs>;
}
