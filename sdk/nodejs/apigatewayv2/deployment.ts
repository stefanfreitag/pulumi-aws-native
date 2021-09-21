// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ApiGatewayV2::Deployment
 *
 * @deprecated Deployment is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class Deployment extends pulumi.CustomResource {
    /**
     * Get an existing Deployment resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Deployment {
        pulumi.log.warn("Deployment is deprecated: Deployment is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new Deployment(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:apigatewayv2:Deployment';

    /**
     * Returns true if the given object is an instance of Deployment.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Deployment {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Deployment.__pulumiType;
    }

    public readonly apiId!: pulumi.Output<string>;
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly stageName!: pulumi.Output<string | undefined>;

    /**
     * Create a Deployment resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated Deployment is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: DeploymentArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("Deployment is deprecated: Deployment is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.apiId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'apiId'");
            }
            inputs["apiId"] = args ? args.apiId : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["stageName"] = args ? args.stageName : undefined;
        } else {
            inputs["apiId"] = undefined /*out*/;
            inputs["description"] = undefined /*out*/;
            inputs["stageName"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Deployment.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Deployment resource.
 */
export interface DeploymentArgs {
    apiId: pulumi.Input<string>;
    description?: pulumi.Input<string>;
    stageName?: pulumi.Input<string>;
}
