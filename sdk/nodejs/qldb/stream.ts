// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::QLDB::Stream.
 */
export class Stream extends pulumi.CustomResource {
    /**
     * Get an existing Stream resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Stream {
        return new Stream(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:qldb:Stream';

    /**
     * Returns true if the given object is an instance of Stream.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Stream {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Stream.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly exclusiveEndTime!: pulumi.Output<string | undefined>;
    public readonly inclusiveStartTime!: pulumi.Output<string>;
    public readonly kinesisConfiguration!: pulumi.Output<outputs.qldb.StreamKinesisConfiguration>;
    public readonly ledgerName!: pulumi.Output<string>;
    public readonly roleArn!: pulumi.Output<string>;
    public readonly streamName!: pulumi.Output<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.qldb.StreamTag[] | undefined>;

    /**
     * Create a Stream resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: StreamArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.inclusiveStartTime === undefined) && !opts.urn) {
                throw new Error("Missing required property 'inclusiveStartTime'");
            }
            if ((!args || args.kinesisConfiguration === undefined) && !opts.urn) {
                throw new Error("Missing required property 'kinesisConfiguration'");
            }
            if ((!args || args.ledgerName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'ledgerName'");
            }
            if ((!args || args.roleArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'roleArn'");
            }
            if ((!args || args.streamName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'streamName'");
            }
            inputs["exclusiveEndTime"] = args ? args.exclusiveEndTime : undefined;
            inputs["inclusiveStartTime"] = args ? args.inclusiveStartTime : undefined;
            inputs["kinesisConfiguration"] = args ? args.kinesisConfiguration : undefined;
            inputs["ledgerName"] = args ? args.ledgerName : undefined;
            inputs["roleArn"] = args ? args.roleArn : undefined;
            inputs["streamName"] = args ? args.streamName : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["arn"] = undefined /*out*/;
        } else {
            inputs["arn"] = undefined /*out*/;
            inputs["exclusiveEndTime"] = undefined /*out*/;
            inputs["inclusiveStartTime"] = undefined /*out*/;
            inputs["kinesisConfiguration"] = undefined /*out*/;
            inputs["ledgerName"] = undefined /*out*/;
            inputs["roleArn"] = undefined /*out*/;
            inputs["streamName"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Stream.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Stream resource.
 */
export interface StreamArgs {
    exclusiveEndTime?: pulumi.Input<string>;
    inclusiveStartTime: pulumi.Input<string>;
    kinesisConfiguration: pulumi.Input<inputs.qldb.StreamKinesisConfigurationArgs>;
    ledgerName: pulumi.Input<string>;
    roleArn: pulumi.Input<string>;
    streamName: pulumi.Input<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.qldb.StreamTagArgs>[]>;
}
