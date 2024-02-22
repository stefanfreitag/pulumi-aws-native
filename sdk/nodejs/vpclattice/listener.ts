// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Creates a listener for a service. Before you start using your Amazon VPC Lattice service, you must add one or more listeners. A listener is a process that checks for connection requests to your services.
 */
export class Listener extends pulumi.CustomResource {
    /**
     * Get an existing Listener resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Listener {
        return new Listener(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:vpclattice:Listener';

    /**
     * Returns true if the given object is an instance of Listener.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Listener {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Listener.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly defaultAction!: pulumi.Output<outputs.vpclattice.ListenerDefaultAction>;
    public readonly name!: pulumi.Output<string | undefined>;
    public readonly port!: pulumi.Output<number | undefined>;
    public readonly protocol!: pulumi.Output<enums.vpclattice.ListenerProtocol>;
    public /*out*/ readonly serviceArn!: pulumi.Output<string>;
    public /*out*/ readonly serviceId!: pulumi.Output<string>;
    public readonly serviceIdentifier!: pulumi.Output<string | undefined>;
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a Listener resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ListenerArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.defaultAction === undefined) && !opts.urn) {
                throw new Error("Missing required property 'defaultAction'");
            }
            if ((!args || args.protocol === undefined) && !opts.urn) {
                throw new Error("Missing required property 'protocol'");
            }
            resourceInputs["defaultAction"] = args ? args.defaultAction : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["port"] = args ? args.port : undefined;
            resourceInputs["protocol"] = args ? args.protocol : undefined;
            resourceInputs["serviceIdentifier"] = args ? args.serviceIdentifier : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["serviceArn"] = undefined /*out*/;
            resourceInputs["serviceId"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["defaultAction"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["port"] = undefined /*out*/;
            resourceInputs["protocol"] = undefined /*out*/;
            resourceInputs["serviceArn"] = undefined /*out*/;
            resourceInputs["serviceId"] = undefined /*out*/;
            resourceInputs["serviceIdentifier"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["name", "port", "protocol", "serviceIdentifier"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Listener.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Listener resource.
 */
export interface ListenerArgs {
    defaultAction: pulumi.Input<inputs.vpclattice.ListenerDefaultActionArgs>;
    name?: pulumi.Input<string>;
    port?: pulumi.Input<number>;
    protocol: pulumi.Input<enums.vpclattice.ListenerProtocol>;
    serviceIdentifier?: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
