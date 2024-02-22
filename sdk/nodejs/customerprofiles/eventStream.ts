// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * An Event Stream resource of Amazon Connect Customer Profiles
 */
export class EventStream extends pulumi.CustomResource {
    /**
     * Get an existing EventStream resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): EventStream {
        return new EventStream(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:customerprofiles:EventStream';

    /**
     * Returns true if the given object is an instance of EventStream.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is EventStream {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === EventStream.__pulumiType;
    }

    /**
     * The timestamp of when the export was created.
     */
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    /**
     * Details regarding the Kinesis stream.
     */
    public /*out*/ readonly destinationDetails!: pulumi.Output<outputs.customerprofiles.DestinationDetailsProperties>;
    /**
     * The unique name of the domain.
     */
    public readonly domainName!: pulumi.Output<string>;
    /**
     * A unique identifier for the event stream.
     */
    public /*out*/ readonly eventStreamArn!: pulumi.Output<string>;
    /**
     * The name of the event stream.
     */
    public readonly eventStreamName!: pulumi.Output<string>;
    /**
     * The operational state of destination stream for export.
     */
    public /*out*/ readonly state!: pulumi.Output<enums.customerprofiles.EventStreamState>;
    /**
     * The tags used to organize, track, or control access for this resource.
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;
    public readonly uri!: pulumi.Output<string>;

    /**
     * Create a EventStream resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: EventStreamArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.domainName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'domainName'");
            }
            if ((!args || args.uri === undefined) && !opts.urn) {
                throw new Error("Missing required property 'uri'");
            }
            resourceInputs["domainName"] = args ? args.domainName : undefined;
            resourceInputs["eventStreamName"] = args ? args.eventStreamName : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["uri"] = args ? args.uri : undefined;
            resourceInputs["createdAt"] = undefined /*out*/;
            resourceInputs["destinationDetails"] = undefined /*out*/;
            resourceInputs["eventStreamArn"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
        } else {
            resourceInputs["createdAt"] = undefined /*out*/;
            resourceInputs["destinationDetails"] = undefined /*out*/;
            resourceInputs["domainName"] = undefined /*out*/;
            resourceInputs["eventStreamArn"] = undefined /*out*/;
            resourceInputs["eventStreamName"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["uri"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["domainName", "eventStreamName", "uri"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(EventStream.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a EventStream resource.
 */
export interface EventStreamArgs {
    /**
     * The unique name of the domain.
     */
    domainName: pulumi.Input<string>;
    /**
     * The name of the event stream.
     */
    eventStreamName?: pulumi.Input<string>;
    /**
     * The tags used to organize, track, or control access for this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
    uri: pulumi.Input<string>;
}
