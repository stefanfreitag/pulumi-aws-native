// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::EC2::NetworkInsightsPath
 */
export class NetworkInsightsPath extends pulumi.CustomResource {
    /**
     * Get an existing NetworkInsightsPath resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): NetworkInsightsPath {
        return new NetworkInsightsPath(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:NetworkInsightsPath';

    /**
     * Returns true if the given object is an instance of NetworkInsightsPath.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is NetworkInsightsPath {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === NetworkInsightsPath.__pulumiType;
    }

    public /*out*/ readonly createdDate!: pulumi.Output<string>;
    public readonly destination!: pulumi.Output<string | undefined>;
    public /*out*/ readonly destinationArn!: pulumi.Output<string>;
    public readonly destinationIp!: pulumi.Output<string | undefined>;
    public readonly destinationPort!: pulumi.Output<number | undefined>;
    public readonly filterAtDestination!: pulumi.Output<outputs.ec2.NetworkInsightsPathPathFilter | undefined>;
    public readonly filterAtSource!: pulumi.Output<outputs.ec2.NetworkInsightsPathPathFilter | undefined>;
    public /*out*/ readonly networkInsightsPathArn!: pulumi.Output<string>;
    public /*out*/ readonly networkInsightsPathId!: pulumi.Output<string>;
    public readonly protocol!: pulumi.Output<enums.ec2.NetworkInsightsPathProtocol>;
    public readonly source!: pulumi.Output<string>;
    public /*out*/ readonly sourceArn!: pulumi.Output<string>;
    public readonly sourceIp!: pulumi.Output<string | undefined>;
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a NetworkInsightsPath resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: NetworkInsightsPathArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.protocol === undefined) && !opts.urn) {
                throw new Error("Missing required property 'protocol'");
            }
            if ((!args || args.source === undefined) && !opts.urn) {
                throw new Error("Missing required property 'source'");
            }
            resourceInputs["destination"] = args ? args.destination : undefined;
            resourceInputs["destinationIp"] = args ? args.destinationIp : undefined;
            resourceInputs["destinationPort"] = args ? args.destinationPort : undefined;
            resourceInputs["filterAtDestination"] = args ? args.filterAtDestination : undefined;
            resourceInputs["filterAtSource"] = args ? args.filterAtSource : undefined;
            resourceInputs["protocol"] = args ? args.protocol : undefined;
            resourceInputs["source"] = args ? args.source : undefined;
            resourceInputs["sourceIp"] = args ? args.sourceIp : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["createdDate"] = undefined /*out*/;
            resourceInputs["destinationArn"] = undefined /*out*/;
            resourceInputs["networkInsightsPathArn"] = undefined /*out*/;
            resourceInputs["networkInsightsPathId"] = undefined /*out*/;
            resourceInputs["sourceArn"] = undefined /*out*/;
        } else {
            resourceInputs["createdDate"] = undefined /*out*/;
            resourceInputs["destination"] = undefined /*out*/;
            resourceInputs["destinationArn"] = undefined /*out*/;
            resourceInputs["destinationIp"] = undefined /*out*/;
            resourceInputs["destinationPort"] = undefined /*out*/;
            resourceInputs["filterAtDestination"] = undefined /*out*/;
            resourceInputs["filterAtSource"] = undefined /*out*/;
            resourceInputs["networkInsightsPathArn"] = undefined /*out*/;
            resourceInputs["networkInsightsPathId"] = undefined /*out*/;
            resourceInputs["protocol"] = undefined /*out*/;
            resourceInputs["source"] = undefined /*out*/;
            resourceInputs["sourceArn"] = undefined /*out*/;
            resourceInputs["sourceIp"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["destination", "destinationIp", "destinationPort", "filterAtDestination", "filterAtSource", "protocol", "source", "sourceIp"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(NetworkInsightsPath.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a NetworkInsightsPath resource.
 */
export interface NetworkInsightsPathArgs {
    destination?: pulumi.Input<string>;
    destinationIp?: pulumi.Input<string>;
    destinationPort?: pulumi.Input<number>;
    filterAtDestination?: pulumi.Input<inputs.ec2.NetworkInsightsPathPathFilterArgs>;
    filterAtSource?: pulumi.Input<inputs.ec2.NetworkInsightsPathPathFilterArgs>;
    protocol: pulumi.Input<enums.ec2.NetworkInsightsPathProtocol>;
    source: pulumi.Input<string>;
    sourceIp?: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
