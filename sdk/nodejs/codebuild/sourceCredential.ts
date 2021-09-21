// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::CodeBuild::SourceCredential
 *
 * @deprecated SourceCredential is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class SourceCredential extends pulumi.CustomResource {
    /**
     * Get an existing SourceCredential resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): SourceCredential {
        pulumi.log.warn("SourceCredential is deprecated: SourceCredential is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new SourceCredential(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:codebuild:SourceCredential';

    /**
     * Returns true if the given object is an instance of SourceCredential.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is SourceCredential {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === SourceCredential.__pulumiType;
    }

    public readonly authType!: pulumi.Output<string>;
    public readonly serverType!: pulumi.Output<string>;
    public readonly token!: pulumi.Output<string>;
    public readonly username!: pulumi.Output<string | undefined>;

    /**
     * Create a SourceCredential resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated SourceCredential is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: SourceCredentialArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("SourceCredential is deprecated: SourceCredential is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.authType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'authType'");
            }
            if ((!args || args.serverType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serverType'");
            }
            if ((!args || args.token === undefined) && !opts.urn) {
                throw new Error("Missing required property 'token'");
            }
            inputs["authType"] = args ? args.authType : undefined;
            inputs["serverType"] = args ? args.serverType : undefined;
            inputs["token"] = args ? args.token : undefined;
            inputs["username"] = args ? args.username : undefined;
        } else {
            inputs["authType"] = undefined /*out*/;
            inputs["serverType"] = undefined /*out*/;
            inputs["token"] = undefined /*out*/;
            inputs["username"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(SourceCredential.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a SourceCredential resource.
 */
export interface SourceCredentialArgs {
    authType: pulumi.Input<string>;
    serverType: pulumi.Input<string>;
    token: pulumi.Input<string>;
    username?: pulumi.Input<string>;
}
