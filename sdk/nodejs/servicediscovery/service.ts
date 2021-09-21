// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ServiceDiscovery::Service
 *
 * @deprecated Service is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class Service extends pulumi.CustomResource {
    /**
     * Get an existing Service resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Service {
        pulumi.log.warn("Service is deprecated: Service is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new Service(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:servicediscovery:Service';

    /**
     * Returns true if the given object is an instance of Service.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Service {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Service.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly dnsConfig!: pulumi.Output<outputs.servicediscovery.ServiceDnsConfig | undefined>;
    public readonly healthCheckConfig!: pulumi.Output<outputs.servicediscovery.ServiceHealthCheckConfig | undefined>;
    public readonly healthCheckCustomConfig!: pulumi.Output<outputs.servicediscovery.ServiceHealthCheckCustomConfig | undefined>;
    public readonly name!: pulumi.Output<string | undefined>;
    public readonly namespaceId!: pulumi.Output<string | undefined>;
    public readonly tags!: pulumi.Output<outputs.servicediscovery.ServiceTag[] | undefined>;
    public readonly type!: pulumi.Output<string | undefined>;

    /**
     * Create a Service resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated Service is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args?: ServiceArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("Service is deprecated: Service is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            inputs["description"] = args ? args.description : undefined;
            inputs["dnsConfig"] = args ? args.dnsConfig : undefined;
            inputs["healthCheckConfig"] = args ? args.healthCheckConfig : undefined;
            inputs["healthCheckCustomConfig"] = args ? args.healthCheckCustomConfig : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["namespaceId"] = args ? args.namespaceId : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["type"] = args ? args.type : undefined;
            inputs["arn"] = undefined /*out*/;
        } else {
            inputs["arn"] = undefined /*out*/;
            inputs["description"] = undefined /*out*/;
            inputs["dnsConfig"] = undefined /*out*/;
            inputs["healthCheckConfig"] = undefined /*out*/;
            inputs["healthCheckCustomConfig"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["namespaceId"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
            inputs["type"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Service.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Service resource.
 */
export interface ServiceArgs {
    description?: pulumi.Input<string>;
    dnsConfig?: pulumi.Input<inputs.servicediscovery.ServiceDnsConfigArgs>;
    healthCheckConfig?: pulumi.Input<inputs.servicediscovery.ServiceHealthCheckConfigArgs>;
    healthCheckCustomConfig?: pulumi.Input<inputs.servicediscovery.ServiceHealthCheckCustomConfigArgs>;
    name?: pulumi.Input<string>;
    namespaceId?: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.servicediscovery.ServiceTagArgs>[]>;
    type?: pulumi.Input<string>;
}
