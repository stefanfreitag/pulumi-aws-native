// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type Definition for AWS::Forecast::Dataset
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
    public static readonly __pulumiType = 'aws-native:forecast:Dataset';

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

    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * Frequency of data collection. This parameter is required for RELATED_TIME_SERIES
     */
    public readonly dataFrequency!: pulumi.Output<string | undefined>;
    /**
     * A name for the dataset
     */
    public readonly datasetName!: pulumi.Output<string>;
    /**
     * The dataset type
     */
    public readonly datasetType!: pulumi.Output<enums.forecast.DatasetType>;
    /**
     * The domain associated with the dataset
     */
    public readonly domain!: pulumi.Output<enums.forecast.DatasetDomain>;
    public readonly encryptionConfig!: pulumi.Output<outputs.forecast.EncryptionConfigProperties | undefined>;
    public readonly schema!: pulumi.Output<outputs.forecast.SchemaProperties>;
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

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
            if ((!args || args.datasetType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'datasetType'");
            }
            if ((!args || args.domain === undefined) && !opts.urn) {
                throw new Error("Missing required property 'domain'");
            }
            if ((!args || args.schema === undefined) && !opts.urn) {
                throw new Error("Missing required property 'schema'");
            }
            resourceInputs["dataFrequency"] = args ? args.dataFrequency : undefined;
            resourceInputs["datasetName"] = args ? args.datasetName : undefined;
            resourceInputs["datasetType"] = args ? args.datasetType : undefined;
            resourceInputs["domain"] = args ? args.domain : undefined;
            resourceInputs["encryptionConfig"] = args ? args.encryptionConfig : undefined;
            resourceInputs["schema"] = args ? args.schema : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["dataFrequency"] = undefined /*out*/;
            resourceInputs["datasetName"] = undefined /*out*/;
            resourceInputs["datasetType"] = undefined /*out*/;
            resourceInputs["domain"] = undefined /*out*/;
            resourceInputs["encryptionConfig"] = undefined /*out*/;
            resourceInputs["schema"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
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
    /**
     * Frequency of data collection. This parameter is required for RELATED_TIME_SERIES
     */
    dataFrequency?: pulumi.Input<string>;
    /**
     * A name for the dataset
     */
    datasetName?: pulumi.Input<string>;
    /**
     * The dataset type
     */
    datasetType: pulumi.Input<enums.forecast.DatasetType>;
    /**
     * The domain associated with the dataset
     */
    domain: pulumi.Input<enums.forecast.DatasetDomain>;
    encryptionConfig?: pulumi.Input<inputs.forecast.EncryptionConfigPropertiesArgs>;
    schema: pulumi.Input<inputs.forecast.SchemaPropertiesArgs>;
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
