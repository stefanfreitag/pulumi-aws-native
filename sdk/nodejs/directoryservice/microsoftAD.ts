// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::DirectoryService::MicrosoftAD
 *
 * @deprecated MicrosoftAD is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class MicrosoftAD extends pulumi.CustomResource {
    /**
     * Get an existing MicrosoftAD resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): MicrosoftAD {
        pulumi.log.warn("MicrosoftAD is deprecated: MicrosoftAD is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new MicrosoftAD(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:directoryservice:MicrosoftAD';

    /**
     * Returns true if the given object is an instance of MicrosoftAD.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is MicrosoftAD {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === MicrosoftAD.__pulumiType;
    }

    public /*out*/ readonly alias!: pulumi.Output<string>;
    public readonly createAlias!: pulumi.Output<boolean | undefined>;
    public /*out*/ readonly dnsIpAddresses!: pulumi.Output<string[]>;
    public readonly edition!: pulumi.Output<string | undefined>;
    public readonly enableSso!: pulumi.Output<boolean | undefined>;
    public readonly name!: pulumi.Output<string>;
    public readonly password!: pulumi.Output<string>;
    public readonly shortName!: pulumi.Output<string | undefined>;
    public readonly vpcSettings!: pulumi.Output<outputs.directoryservice.MicrosoftADVpcSettings>;

    /**
     * Create a MicrosoftAD resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated MicrosoftAD is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: MicrosoftADArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("MicrosoftAD is deprecated: MicrosoftAD is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            if ((!args || args.password === undefined) && !opts.urn) {
                throw new Error("Missing required property 'password'");
            }
            if ((!args || args.vpcSettings === undefined) && !opts.urn) {
                throw new Error("Missing required property 'vpcSettings'");
            }
            inputs["createAlias"] = args ? args.createAlias : undefined;
            inputs["edition"] = args ? args.edition : undefined;
            inputs["enableSso"] = args ? args.enableSso : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["password"] = args ? args.password : undefined;
            inputs["shortName"] = args ? args.shortName : undefined;
            inputs["vpcSettings"] = args ? args.vpcSettings : undefined;
            inputs["alias"] = undefined /*out*/;
            inputs["dnsIpAddresses"] = undefined /*out*/;
        } else {
            inputs["alias"] = undefined /*out*/;
            inputs["createAlias"] = undefined /*out*/;
            inputs["dnsIpAddresses"] = undefined /*out*/;
            inputs["edition"] = undefined /*out*/;
            inputs["enableSso"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["password"] = undefined /*out*/;
            inputs["shortName"] = undefined /*out*/;
            inputs["vpcSettings"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(MicrosoftAD.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a MicrosoftAD resource.
 */
export interface MicrosoftADArgs {
    createAlias?: pulumi.Input<boolean>;
    edition?: pulumi.Input<string>;
    enableSso?: pulumi.Input<boolean>;
    name: pulumi.Input<string>;
    password: pulumi.Input<string>;
    shortName?: pulumi.Input<string>;
    vpcSettings: pulumi.Input<inputs.directoryservice.MicrosoftADVpcSettingsArgs>;
}
