// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * AWS Route53 Recovery Control Routing Control resource schema .
 */
export class RoutingControl extends pulumi.CustomResource {
    /**
     * Get an existing RoutingControl resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): RoutingControl {
        return new RoutingControl(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:route53recoverycontrol:RoutingControl';

    /**
     * Returns true if the given object is an instance of RoutingControl.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is RoutingControl {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === RoutingControl.__pulumiType;
    }

    /**
     * Arn associated with Control Panel
     */
    public readonly clusterArn!: pulumi.Output<string | undefined>;
    /**
     * The Amazon Resource Name (ARN) of the control panel.
     */
    public readonly controlPanelArn!: pulumi.Output<string | undefined>;
    /**
     * The name of the routing control. You can use any non-white space character in the name.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The Amazon Resource Name (ARN) of the routing control.
     */
    public /*out*/ readonly routingControlArn!: pulumi.Output<string>;
    /**
     * The deployment status of the routing control. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.
     */
    public /*out*/ readonly status!: pulumi.Output<enums.route53recoverycontrol.RoutingControlStatus>;

    /**
     * Create a RoutingControl resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RoutingControlArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            inputs["clusterArn"] = args ? args.clusterArn : undefined;
            inputs["controlPanelArn"] = args ? args.controlPanelArn : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["routingControlArn"] = undefined /*out*/;
            inputs["status"] = undefined /*out*/;
        } else {
            inputs["clusterArn"] = undefined /*out*/;
            inputs["controlPanelArn"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["routingControlArn"] = undefined /*out*/;
            inputs["status"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(RoutingControl.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a RoutingControl resource.
 */
export interface RoutingControlArgs {
    /**
     * Arn associated with Control Panel
     */
    clusterArn?: pulumi.Input<string>;
    /**
     * The Amazon Resource Name (ARN) of the control panel.
     */
    controlPanelArn?: pulumi.Input<string>;
    /**
     * The name of the routing control. You can use any non-white space character in the name.
     */
    name: pulumi.Input<string>;
}
