// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * A replication configuration that you later provide to configure and start a AWS DMS Serverless replication
 */
export class ReplicationConfig extends pulumi.CustomResource {
    /**
     * Get an existing ReplicationConfig resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ReplicationConfig {
        return new ReplicationConfig(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:dms:ReplicationConfig';

    /**
     * Returns true if the given object is an instance of ReplicationConfig.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ReplicationConfig {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ReplicationConfig.__pulumiType;
    }

    public readonly computeConfig!: pulumi.Output<outputs.dms.ReplicationConfigComputeConfig | undefined>;
    /**
     * The Amazon Resource Name (ARN) of the Replication Config
     */
    public readonly replicationConfigArn!: pulumi.Output<string | undefined>;
    /**
     * A unique identifier of replication configuration
     */
    public readonly replicationConfigIdentifier!: pulumi.Output<string | undefined>;
    /**
     * JSON settings for Servereless replications that are provisioned using this replication configuration
     *
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::DMS::ReplicationConfig` for more information about the expected schema for this property.
     */
    public readonly replicationSettings!: pulumi.Output<any | undefined>;
    /**
     * The type of AWS DMS Serverless replication to provision using this replication configuration
     */
    public readonly replicationType!: pulumi.Output<enums.dms.ReplicationConfigReplicationType | undefined>;
    /**
     * A unique value or name that you get set for a given resource that can be used to construct an Amazon Resource Name (ARN) for that resource
     */
    public readonly resourceIdentifier!: pulumi.Output<string | undefined>;
    /**
     * The Amazon Resource Name (ARN) of the source endpoint for this AWS DMS Serverless replication configuration
     */
    public readonly sourceEndpointArn!: pulumi.Output<string | undefined>;
    /**
     * JSON settings for specifying supplemental data
     *
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::DMS::ReplicationConfig` for more information about the expected schema for this property.
     */
    public readonly supplementalSettings!: pulumi.Output<any | undefined>;
    /**
     * JSON table mappings for AWS DMS Serverless replications that are provisioned using this replication configuration
     *
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::DMS::ReplicationConfig` for more information about the expected schema for this property.
     */
    public readonly tableMappings!: pulumi.Output<any | undefined>;
    /**
     * <p>Contains a map of the key-value pairs for the resource tag or tags assigned to the dataset.</p>
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;
    /**
     * The Amazon Resource Name (ARN) of the target endpoint for this AWS DMS Serverless replication configuration
     */
    public readonly targetEndpointArn!: pulumi.Output<string | undefined>;

    /**
     * Create a ReplicationConfig resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ReplicationConfigArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["computeConfig"] = args ? args.computeConfig : undefined;
            resourceInputs["replicationConfigArn"] = args ? args.replicationConfigArn : undefined;
            resourceInputs["replicationConfigIdentifier"] = args ? args.replicationConfigIdentifier : undefined;
            resourceInputs["replicationSettings"] = args ? args.replicationSettings : undefined;
            resourceInputs["replicationType"] = args ? args.replicationType : undefined;
            resourceInputs["resourceIdentifier"] = args ? args.resourceIdentifier : undefined;
            resourceInputs["sourceEndpointArn"] = args ? args.sourceEndpointArn : undefined;
            resourceInputs["supplementalSettings"] = args ? args.supplementalSettings : undefined;
            resourceInputs["tableMappings"] = args ? args.tableMappings : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["targetEndpointArn"] = args ? args.targetEndpointArn : undefined;
        } else {
            resourceInputs["computeConfig"] = undefined /*out*/;
            resourceInputs["replicationConfigArn"] = undefined /*out*/;
            resourceInputs["replicationConfigIdentifier"] = undefined /*out*/;
            resourceInputs["replicationSettings"] = undefined /*out*/;
            resourceInputs["replicationType"] = undefined /*out*/;
            resourceInputs["resourceIdentifier"] = undefined /*out*/;
            resourceInputs["sourceEndpointArn"] = undefined /*out*/;
            resourceInputs["supplementalSettings"] = undefined /*out*/;
            resourceInputs["tableMappings"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["targetEndpointArn"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["resourceIdentifier"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(ReplicationConfig.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ReplicationConfig resource.
 */
export interface ReplicationConfigArgs {
    computeConfig?: pulumi.Input<inputs.dms.ReplicationConfigComputeConfigArgs>;
    /**
     * The Amazon Resource Name (ARN) of the Replication Config
     */
    replicationConfigArn?: pulumi.Input<string>;
    /**
     * A unique identifier of replication configuration
     */
    replicationConfigIdentifier?: pulumi.Input<string>;
    /**
     * JSON settings for Servereless replications that are provisioned using this replication configuration
     *
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::DMS::ReplicationConfig` for more information about the expected schema for this property.
     */
    replicationSettings?: any;
    /**
     * The type of AWS DMS Serverless replication to provision using this replication configuration
     */
    replicationType?: pulumi.Input<enums.dms.ReplicationConfigReplicationType>;
    /**
     * A unique value or name that you get set for a given resource that can be used to construct an Amazon Resource Name (ARN) for that resource
     */
    resourceIdentifier?: pulumi.Input<string>;
    /**
     * The Amazon Resource Name (ARN) of the source endpoint for this AWS DMS Serverless replication configuration
     */
    sourceEndpointArn?: pulumi.Input<string>;
    /**
     * JSON settings for specifying supplemental data
     *
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::DMS::ReplicationConfig` for more information about the expected schema for this property.
     */
    supplementalSettings?: any;
    /**
     * JSON table mappings for AWS DMS Serverless replications that are provisioned using this replication configuration
     *
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::DMS::ReplicationConfig` for more information about the expected schema for this property.
     */
    tableMappings?: any;
    /**
     * <p>Contains a map of the key-value pairs for the resource tag or tags assigned to the dataset.</p>
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
    /**
     * The Amazon Resource Name (ARN) of the target endpoint for this AWS DMS Serverless replication configuration
     */
    targetEndpointArn?: pulumi.Input<string>;
}
