// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::IAM::Role
 *
 * @deprecated Role is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class Role extends pulumi.CustomResource {
    /**
     * Get an existing Role resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Role {
        pulumi.log.warn("Role is deprecated: Role is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new Role(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:iam:Role';

    /**
     * Returns true if the given object is an instance of Role.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Role {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Role.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly assumeRolePolicyDocument!: pulumi.Output<any>;
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly managedPolicyArns!: pulumi.Output<string[] | undefined>;
    public readonly maxSessionDuration!: pulumi.Output<number | undefined>;
    public readonly path!: pulumi.Output<string | undefined>;
    public readonly permissionsBoundary!: pulumi.Output<string | undefined>;
    public readonly policies!: pulumi.Output<outputs.iam.RolePolicy[] | undefined>;
    public /*out*/ readonly roleId!: pulumi.Output<string>;
    public readonly roleName!: pulumi.Output<string | undefined>;
    public readonly tags!: pulumi.Output<outputs.iam.RoleTag[] | undefined>;

    /**
     * Create a Role resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated Role is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: RoleArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("Role is deprecated: Role is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.assumeRolePolicyDocument === undefined) && !opts.urn) {
                throw new Error("Missing required property 'assumeRolePolicyDocument'");
            }
            inputs["assumeRolePolicyDocument"] = args ? args.assumeRolePolicyDocument : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["managedPolicyArns"] = args ? args.managedPolicyArns : undefined;
            inputs["maxSessionDuration"] = args ? args.maxSessionDuration : undefined;
            inputs["path"] = args ? args.path : undefined;
            inputs["permissionsBoundary"] = args ? args.permissionsBoundary : undefined;
            inputs["policies"] = args ? args.policies : undefined;
            inputs["roleName"] = args ? args.roleName : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["roleId"] = undefined /*out*/;
        } else {
            inputs["arn"] = undefined /*out*/;
            inputs["assumeRolePolicyDocument"] = undefined /*out*/;
            inputs["description"] = undefined /*out*/;
            inputs["managedPolicyArns"] = undefined /*out*/;
            inputs["maxSessionDuration"] = undefined /*out*/;
            inputs["path"] = undefined /*out*/;
            inputs["permissionsBoundary"] = undefined /*out*/;
            inputs["policies"] = undefined /*out*/;
            inputs["roleId"] = undefined /*out*/;
            inputs["roleName"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Role.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Role resource.
 */
export interface RoleArgs {
    assumeRolePolicyDocument: any;
    description?: pulumi.Input<string>;
    managedPolicyArns?: pulumi.Input<pulumi.Input<string>[]>;
    maxSessionDuration?: pulumi.Input<number>;
    path?: pulumi.Input<string>;
    permissionsBoundary?: pulumi.Input<string>;
    policies?: pulumi.Input<pulumi.Input<inputs.iam.RolePolicyArgs>[]>;
    roleName?: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.iam.RoleTagArgs>[]>;
}
