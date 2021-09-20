// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Kinesis::Stream
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
    public static readonly __pulumiType = 'aws-native:kinesis:Stream';

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

    /**
     * The Amazon resource name (ARN) of the Kinesis stream
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The name of the Kinesis stream.
     */
    public readonly name!: pulumi.Output<string | undefined>;
    /**
     * The number of hours for the data records that are stored in shards to remain accessible.
     */
    public readonly retentionPeriodHours!: pulumi.Output<number | undefined>;
    /**
     * The number of shards that the stream uses.
     */
    public readonly shardCount!: pulumi.Output<number>;
    /**
     * When specified, enables or updates server-side encryption using an AWS KMS key for a specified stream.
     */
    public readonly streamEncryption!: pulumi.Output<outputs.kinesis.StreamStreamEncryption | undefined>;
    /**
     * An arbitrary set of tags (key–value pairs) to associate with the Kinesis stream.
     */
    public readonly tags!: pulumi.Output<outputs.kinesis.StreamTag[] | undefined>;

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
            if ((!args || args.shardCount === undefined) && !opts.urn) {
                throw new Error("Missing required property 'shardCount'");
            }
            inputs["name"] = args ? args.name : undefined;
            inputs["retentionPeriodHours"] = args ? args.retentionPeriodHours : undefined;
            inputs["shardCount"] = args ? args.shardCount : undefined;
            inputs["streamEncryption"] = args ? args.streamEncryption : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["arn"] = undefined /*out*/;
        } else {
            inputs["arn"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["retentionPeriodHours"] = undefined /*out*/;
            inputs["shardCount"] = undefined /*out*/;
            inputs["streamEncryption"] = undefined /*out*/;
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
    /**
     * The name of the Kinesis stream.
     */
    name?: pulumi.Input<string>;
    /**
     * The number of hours for the data records that are stored in shards to remain accessible.
     */
    retentionPeriodHours?: pulumi.Input<number>;
    /**
     * The number of shards that the stream uses.
     */
    shardCount: pulumi.Input<number>;
    /**
     * When specified, enables or updates server-side encryption using an AWS KMS key for a specified stream.
     */
    streamEncryption?: pulumi.Input<inputs.kinesis.StreamStreamEncryptionArgs>;
    /**
     * An arbitrary set of tags (key–value pairs) to associate with the Kinesis stream.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.kinesis.StreamTagArgs>[]>;
}
