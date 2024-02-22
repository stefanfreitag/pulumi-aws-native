// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * An OpenSearch Ingestion Service Data Prepper pipeline running Data Prepper.
 */
export class Pipeline extends pulumi.CustomResource {
    /**
     * Get an existing Pipeline resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Pipeline {
        return new Pipeline(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:osis:Pipeline';

    /**
     * Returns true if the given object is an instance of Pipeline.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Pipeline {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Pipeline.__pulumiType;
    }

    public readonly bufferOptions!: pulumi.Output<outputs.osis.PipelineBufferOptions | undefined>;
    public readonly encryptionAtRestOptions!: pulumi.Output<outputs.osis.PipelineEncryptionAtRestOptions | undefined>;
    /**
     * A list of endpoints that can be used for ingesting data into a pipeline
     */
    public /*out*/ readonly ingestEndpointUrls!: pulumi.Output<string[]>;
    public readonly logPublishingOptions!: pulumi.Output<outputs.osis.PipelineLogPublishingOptions | undefined>;
    /**
     * The maximum pipeline capacity, in Ingestion Compute Units (ICUs).
     */
    public readonly maxUnits!: pulumi.Output<number>;
    /**
     * The minimum pipeline capacity, in Ingestion Compute Units (ICUs).
     */
    public readonly minUnits!: pulumi.Output<number>;
    /**
     * The Amazon Resource Name (ARN) of the pipeline.
     */
    public /*out*/ readonly pipelineArn!: pulumi.Output<string>;
    /**
     * The Data Prepper pipeline configuration in YAML format.
     */
    public readonly pipelineConfigurationBody!: pulumi.Output<string>;
    /**
     * Name of the OpenSearch Ingestion Service pipeline to create. Pipeline names are unique across the pipelines owned by an account within an AWS Region.
     */
    public readonly pipelineName!: pulumi.Output<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;
    /**
     * The VPC interface endpoints that have access to the pipeline.
     */
    public /*out*/ readonly vpcEndpoints!: pulumi.Output<outputs.osis.PipelineVpcEndpoint[]>;
    public readonly vpcOptions!: pulumi.Output<outputs.osis.PipelineVpcOptions | undefined>;

    /**
     * Create a Pipeline resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PipelineArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.maxUnits === undefined) && !opts.urn) {
                throw new Error("Missing required property 'maxUnits'");
            }
            if ((!args || args.minUnits === undefined) && !opts.urn) {
                throw new Error("Missing required property 'minUnits'");
            }
            if ((!args || args.pipelineConfigurationBody === undefined) && !opts.urn) {
                throw new Error("Missing required property 'pipelineConfigurationBody'");
            }
            resourceInputs["bufferOptions"] = args ? args.bufferOptions : undefined;
            resourceInputs["encryptionAtRestOptions"] = args ? args.encryptionAtRestOptions : undefined;
            resourceInputs["logPublishingOptions"] = args ? args.logPublishingOptions : undefined;
            resourceInputs["maxUnits"] = args ? args.maxUnits : undefined;
            resourceInputs["minUnits"] = args ? args.minUnits : undefined;
            resourceInputs["pipelineConfigurationBody"] = args ? args.pipelineConfigurationBody : undefined;
            resourceInputs["pipelineName"] = args ? args.pipelineName : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["vpcOptions"] = args ? args.vpcOptions : undefined;
            resourceInputs["ingestEndpointUrls"] = undefined /*out*/;
            resourceInputs["pipelineArn"] = undefined /*out*/;
            resourceInputs["vpcEndpoints"] = undefined /*out*/;
        } else {
            resourceInputs["bufferOptions"] = undefined /*out*/;
            resourceInputs["encryptionAtRestOptions"] = undefined /*out*/;
            resourceInputs["ingestEndpointUrls"] = undefined /*out*/;
            resourceInputs["logPublishingOptions"] = undefined /*out*/;
            resourceInputs["maxUnits"] = undefined /*out*/;
            resourceInputs["minUnits"] = undefined /*out*/;
            resourceInputs["pipelineArn"] = undefined /*out*/;
            resourceInputs["pipelineConfigurationBody"] = undefined /*out*/;
            resourceInputs["pipelineName"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["vpcEndpoints"] = undefined /*out*/;
            resourceInputs["vpcOptions"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["pipelineName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Pipeline.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Pipeline resource.
 */
export interface PipelineArgs {
    bufferOptions?: pulumi.Input<inputs.osis.PipelineBufferOptionsArgs>;
    encryptionAtRestOptions?: pulumi.Input<inputs.osis.PipelineEncryptionAtRestOptionsArgs>;
    logPublishingOptions?: pulumi.Input<inputs.osis.PipelineLogPublishingOptionsArgs>;
    /**
     * The maximum pipeline capacity, in Ingestion Compute Units (ICUs).
     */
    maxUnits: pulumi.Input<number>;
    /**
     * The minimum pipeline capacity, in Ingestion Compute Units (ICUs).
     */
    minUnits: pulumi.Input<number>;
    /**
     * The Data Prepper pipeline configuration in YAML format.
     */
    pipelineConfigurationBody: pulumi.Input<string>;
    /**
     * Name of the OpenSearch Ingestion Service pipeline to create. Pipeline names are unique across the pipelines owned by an account within an AWS Region.
     */
    pipelineName?: pulumi.Input<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
    vpcOptions?: pulumi.Input<inputs.osis.PipelineVpcOptionsArgs>;
}
