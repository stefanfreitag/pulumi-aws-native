// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Definition of AWS::MediaPackageV2::OriginEndpoint Resource Type
 */
export class OriginEndpoint extends pulumi.CustomResource {
    /**
     * Get an existing OriginEndpoint resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): OriginEndpoint {
        return new OriginEndpoint(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:mediapackagev2:OriginEndpoint';

    /**
     * Returns true if the given object is an instance of OriginEndpoint.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is OriginEndpoint {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === OriginEndpoint.__pulumiType;
    }

    /**
     * <p>The Amazon Resource Name (ARN) associated with the resource.</p>
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly channelGroupName!: pulumi.Output<string | undefined>;
    public readonly channelName!: pulumi.Output<string | undefined>;
    public readonly containerType!: pulumi.Output<enums.mediapackagev2.OriginEndpointContainerType>;
    /**
     * <p>The date and time the origin endpoint was created.</p>
     */
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    /**
     * <p>Enter any descriptive text that helps you to identify the origin endpoint.</p>
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * <p>An HTTP live streaming (HLS) manifest configuration.</p>
     */
    public readonly hlsManifests!: pulumi.Output<outputs.mediapackagev2.OriginEndpointHlsManifestConfiguration[] | undefined>;
    /**
     * <p>A low-latency HLS manifest configuration.</p>
     */
    public readonly lowLatencyHlsManifests!: pulumi.Output<outputs.mediapackagev2.OriginEndpointLowLatencyHlsManifestConfiguration[] | undefined>;
    /**
     * <p>The date and time the origin endpoint was modified.</p>
     */
    public /*out*/ readonly modifiedAt!: pulumi.Output<string>;
    public readonly originEndpointName!: pulumi.Output<string | undefined>;
    public readonly segment!: pulumi.Output<outputs.mediapackagev2.OriginEndpointSegment | undefined>;
    /**
     * <p>The size of the window (in seconds) to create a window of the live stream that's available for on-demand viewing. Viewers can start-over or catch-up on content that falls within the window. The maximum startover window is 1,209,600 seconds (14 days).</p>
     */
    public readonly startoverWindowSeconds!: pulumi.Output<number | undefined>;
    public readonly tags!: pulumi.Output<outputs.mediapackagev2.OriginEndpointTag[] | undefined>;

    /**
     * Create a OriginEndpoint resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: OriginEndpointArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.containerType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'containerType'");
            }
            resourceInputs["channelGroupName"] = args ? args.channelGroupName : undefined;
            resourceInputs["channelName"] = args ? args.channelName : undefined;
            resourceInputs["containerType"] = args ? args.containerType : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["hlsManifests"] = args ? args.hlsManifests : undefined;
            resourceInputs["lowLatencyHlsManifests"] = args ? args.lowLatencyHlsManifests : undefined;
            resourceInputs["originEndpointName"] = args ? args.originEndpointName : undefined;
            resourceInputs["segment"] = args ? args.segment : undefined;
            resourceInputs["startoverWindowSeconds"] = args ? args.startoverWindowSeconds : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["createdAt"] = undefined /*out*/;
            resourceInputs["modifiedAt"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["channelGroupName"] = undefined /*out*/;
            resourceInputs["channelName"] = undefined /*out*/;
            resourceInputs["containerType"] = undefined /*out*/;
            resourceInputs["createdAt"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["hlsManifests"] = undefined /*out*/;
            resourceInputs["lowLatencyHlsManifests"] = undefined /*out*/;
            resourceInputs["modifiedAt"] = undefined /*out*/;
            resourceInputs["originEndpointName"] = undefined /*out*/;
            resourceInputs["segment"] = undefined /*out*/;
            resourceInputs["startoverWindowSeconds"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["channelGroupName", "channelName", "originEndpointName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(OriginEndpoint.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a OriginEndpoint resource.
 */
export interface OriginEndpointArgs {
    channelGroupName?: pulumi.Input<string>;
    channelName?: pulumi.Input<string>;
    containerType: pulumi.Input<enums.mediapackagev2.OriginEndpointContainerType>;
    /**
     * <p>Enter any descriptive text that helps you to identify the origin endpoint.</p>
     */
    description?: pulumi.Input<string>;
    /**
     * <p>An HTTP live streaming (HLS) manifest configuration.</p>
     */
    hlsManifests?: pulumi.Input<pulumi.Input<inputs.mediapackagev2.OriginEndpointHlsManifestConfigurationArgs>[]>;
    /**
     * <p>A low-latency HLS manifest configuration.</p>
     */
    lowLatencyHlsManifests?: pulumi.Input<pulumi.Input<inputs.mediapackagev2.OriginEndpointLowLatencyHlsManifestConfigurationArgs>[]>;
    originEndpointName?: pulumi.Input<string>;
    segment?: pulumi.Input<inputs.mediapackagev2.OriginEndpointSegmentArgs>;
    /**
     * <p>The size of the window (in seconds) to create a window of the live stream that's available for on-demand viewing. Viewers can start-over or catch-up on content that falls within the window. The maximum startover window is 1,209,600 seconds (14 days).</p>
     */
    startoverWindowSeconds?: pulumi.Input<number>;
    tags?: pulumi.Input<pulumi.Input<inputs.mediapackagev2.OriginEndpointTagArgs>[]>;
}
