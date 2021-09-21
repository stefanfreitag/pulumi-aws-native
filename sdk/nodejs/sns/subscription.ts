// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::SNS::Subscription
 *
 * @deprecated Subscription is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class Subscription extends pulumi.CustomResource {
    /**
     * Get an existing Subscription resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Subscription {
        pulumi.log.warn("Subscription is deprecated: Subscription is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new Subscription(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:sns:Subscription';

    /**
     * Returns true if the given object is an instance of Subscription.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Subscription {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Subscription.__pulumiType;
    }

    public readonly deliveryPolicy!: pulumi.Output<any | undefined>;
    public readonly endpoint!: pulumi.Output<string | undefined>;
    public readonly filterPolicy!: pulumi.Output<any | undefined>;
    public readonly protocol!: pulumi.Output<string>;
    public readonly rawMessageDelivery!: pulumi.Output<boolean | undefined>;
    public readonly redrivePolicy!: pulumi.Output<any | undefined>;
    public readonly region!: pulumi.Output<string | undefined>;
    public readonly subscriptionRoleArn!: pulumi.Output<string | undefined>;
    public readonly topicArn!: pulumi.Output<string>;

    /**
     * Create a Subscription resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated Subscription is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: SubscriptionArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("Subscription is deprecated: Subscription is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.protocol === undefined) && !opts.urn) {
                throw new Error("Missing required property 'protocol'");
            }
            if ((!args || args.topicArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'topicArn'");
            }
            inputs["deliveryPolicy"] = args ? args.deliveryPolicy : undefined;
            inputs["endpoint"] = args ? args.endpoint : undefined;
            inputs["filterPolicy"] = args ? args.filterPolicy : undefined;
            inputs["protocol"] = args ? args.protocol : undefined;
            inputs["rawMessageDelivery"] = args ? args.rawMessageDelivery : undefined;
            inputs["redrivePolicy"] = args ? args.redrivePolicy : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["subscriptionRoleArn"] = args ? args.subscriptionRoleArn : undefined;
            inputs["topicArn"] = args ? args.topicArn : undefined;
        } else {
            inputs["deliveryPolicy"] = undefined /*out*/;
            inputs["endpoint"] = undefined /*out*/;
            inputs["filterPolicy"] = undefined /*out*/;
            inputs["protocol"] = undefined /*out*/;
            inputs["rawMessageDelivery"] = undefined /*out*/;
            inputs["redrivePolicy"] = undefined /*out*/;
            inputs["region"] = undefined /*out*/;
            inputs["subscriptionRoleArn"] = undefined /*out*/;
            inputs["topicArn"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Subscription.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Subscription resource.
 */
export interface SubscriptionArgs {
    deliveryPolicy?: any;
    endpoint?: pulumi.Input<string>;
    filterPolicy?: any;
    protocol: pulumi.Input<string>;
    rawMessageDelivery?: pulumi.Input<boolean>;
    redrivePolicy?: any;
    region?: pulumi.Input<string>;
    subscriptionRoleArn?: pulumi.Input<string>;
    topicArn: pulumi.Input<string>;
}
