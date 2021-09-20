// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::CloudFront::PublicKey
 */
export class PublicKey extends pulumi.CustomResource {
    /**
     * Get an existing PublicKey resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): PublicKey {
        return new PublicKey(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:cloudfront:PublicKey';

    /**
     * Returns true if the given object is an instance of PublicKey.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PublicKey {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PublicKey.__pulumiType;
    }

    public /*out*/ readonly createdTime!: pulumi.Output<string>;
    public readonly publicKeyConfig!: pulumi.Output<outputs.cloudfront.PublicKeyPublicKeyConfig>;

    /**
     * Create a PublicKey resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PublicKeyArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.publicKeyConfig === undefined) && !opts.urn) {
                throw new Error("Missing required property 'publicKeyConfig'");
            }
            inputs["publicKeyConfig"] = args ? args.publicKeyConfig : undefined;
            inputs["createdTime"] = undefined /*out*/;
        } else {
            inputs["createdTime"] = undefined /*out*/;
            inputs["publicKeyConfig"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(PublicKey.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a PublicKey resource.
 */
export interface PublicKeyArgs {
    publicKeyConfig: pulumi.Input<inputs.cloudfront.PublicKeyPublicKeyConfigArgs>;
}
