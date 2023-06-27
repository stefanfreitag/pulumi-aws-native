// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::DataSync::StorageSystem.
 */
export class StorageSystem extends pulumi.CustomResource {
    /**
     * Get an existing StorageSystem resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): StorageSystem {
        return new StorageSystem(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:datasync:StorageSystem';

    /**
     * Returns true if the given object is an instance of StorageSystem.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is StorageSystem {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === StorageSystem.__pulumiType;
    }

    /**
     * The ARN of the DataSync agent that connects to and reads from the on-premises storage system's management interface.
     */
    public readonly agentArns!: pulumi.Output<string[]>;
    /**
     * The ARN of the Amazon CloudWatch log group used to monitor and log discovery job events.
     */
    public readonly cloudWatchLogGroupArn!: pulumi.Output<string | undefined>;
    /**
     * Indicates whether the DataSync agent can access the on-premises storage system.
     */
    public /*out*/ readonly connectivityStatus!: pulumi.Output<enums.datasync.StorageSystemConnectivityStatus>;
    /**
     * A familiar name for the on-premises storage system.
     */
    public readonly name!: pulumi.Output<string | undefined>;
    /**
     * The ARN of a secret stored by AWS Secrets Manager.
     */
    public /*out*/ readonly secretsManagerArn!: pulumi.Output<string>;
    public readonly serverConfiguration!: pulumi.Output<outputs.datasync.StorageSystemServerConfiguration>;
    public readonly serverCredentials!: pulumi.Output<outputs.datasync.StorageSystemServerCredentials | undefined>;
    /**
     * The ARN of the on-premises storage system added to DataSync Discovery.
     */
    public /*out*/ readonly storageSystemArn!: pulumi.Output<string>;
    /**
     * The type of on-premises storage system that DataSync Discovery will analyze.
     */
    public readonly systemType!: pulumi.Output<enums.datasync.StorageSystemSystemType>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.datasync.StorageSystemTag[] | undefined>;

    /**
     * Create a StorageSystem resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: StorageSystemArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.agentArns === undefined) && !opts.urn) {
                throw new Error("Missing required property 'agentArns'");
            }
            if ((!args || args.serverConfiguration === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serverConfiguration'");
            }
            if ((!args || args.systemType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'systemType'");
            }
            resourceInputs["agentArns"] = args ? args.agentArns : undefined;
            resourceInputs["cloudWatchLogGroupArn"] = args ? args.cloudWatchLogGroupArn : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["serverConfiguration"] = args ? args.serverConfiguration : undefined;
            resourceInputs["serverCredentials"] = args ? args.serverCredentials : undefined;
            resourceInputs["systemType"] = args ? args.systemType : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["connectivityStatus"] = undefined /*out*/;
            resourceInputs["secretsManagerArn"] = undefined /*out*/;
            resourceInputs["storageSystemArn"] = undefined /*out*/;
        } else {
            resourceInputs["agentArns"] = undefined /*out*/;
            resourceInputs["cloudWatchLogGroupArn"] = undefined /*out*/;
            resourceInputs["connectivityStatus"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["secretsManagerArn"] = undefined /*out*/;
            resourceInputs["serverConfiguration"] = undefined /*out*/;
            resourceInputs["serverCredentials"] = undefined /*out*/;
            resourceInputs["storageSystemArn"] = undefined /*out*/;
            resourceInputs["systemType"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(StorageSystem.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a StorageSystem resource.
 */
export interface StorageSystemArgs {
    /**
     * The ARN of the DataSync agent that connects to and reads from the on-premises storage system's management interface.
     */
    agentArns: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The ARN of the Amazon CloudWatch log group used to monitor and log discovery job events.
     */
    cloudWatchLogGroupArn?: pulumi.Input<string>;
    /**
     * A familiar name for the on-premises storage system.
     */
    name?: pulumi.Input<string>;
    serverConfiguration: pulumi.Input<inputs.datasync.StorageSystemServerConfigurationArgs>;
    serverCredentials?: pulumi.Input<inputs.datasync.StorageSystemServerCredentialsArgs>;
    /**
     * The type of on-premises storage system that DataSync Discovery will analyze.
     */
    systemType: pulumi.Input<enums.datasync.StorageSystemSystemType>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.datasync.StorageSystemTagArgs>[]>;
}
