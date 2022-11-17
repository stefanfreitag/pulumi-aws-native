// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * You can use organizational units (OUs) to group accounts together to administer as a single unit. This greatly simplifies the management of your accounts. For example, you can attach a policy-based control to an OU, and all accounts within the OU automatically inherit the policy. You can create multiple OUs within a single organization, and you can create OUs within other OUs. Each OU can contain multiple accounts, and you can move accounts from one OU to another. However, OU names must be unique within a parent OU or root.
 */
export function getOrganizationalUnit(args: GetOrganizationalUnitArgs, opts?: pulumi.InvokeOptions): Promise<GetOrganizationalUnitResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("aws-native:organizations:getOrganizationalUnit", {
        "id": args.id,
    }, opts);
}

export interface GetOrganizationalUnitArgs {
    /**
     * The unique identifier (ID) associated with this OU.
     */
    id: string;
}

export interface GetOrganizationalUnitResult {
    /**
     * The Amazon Resource Name (ARN) of this OU.
     */
    readonly arn?: string;
    /**
     * The unique identifier (ID) associated with this OU.
     */
    readonly id?: string;
    /**
     * The friendly name of this OU.
     */
    readonly name?: string;
    /**
     * A list of tags that you want to attach to the newly created OU.
     */
    readonly tags?: outputs.organizations.OrganizationalUnitTag[];
}

export function getOrganizationalUnitOutput(args: GetOrganizationalUnitOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetOrganizationalUnitResult> {
    return pulumi.output(args).apply(a => getOrganizationalUnit(a, opts))
}

export interface GetOrganizationalUnitOutputArgs {
    /**
     * The unique identifier (ID) associated with this OU.
     */
    id: pulumi.Input<string>;
}
